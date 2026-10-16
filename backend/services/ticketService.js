const ticketRepository = require('../repositories/ticketRepository');
const eventRepository = require('../repositories/eventRepository');
const ApiError = require('../utils/apiError');

class TicketService {
  async bookTicket(bookingData) {
    const { eventId, userId, attendeeName, tier = 'General Admission', quantity = 1 } = bookingData;

    if (!eventId || !attendeeName) {
      throw ApiError.badRequest('eventId and attendeeName are required');
    }

    const event = await eventRepository.findById(eventId);
    if (!event) {
      throw ApiError.notFound(`Event with ID '${eventId}' not found`);
    }

    if (event.availableCapacity < quantity) {
      throw ApiError.badRequest(`Insufficient capacity. Only ${event.availableCapacity} tickets remaining.`);
    }

    const decremented = await eventRepository.decrementCapacity(eventId, quantity);
    if (!decremented) {
      throw ApiError.conflict('Failed to reserve tickets due to capacity concurrency. Please retry.');
    }

    const tickets = [];
    for (let i = 0; i < quantity; i++) {
      const ticketCode = `ER-${event.title.substring(0, 3).toUpperCase()}-${Math.floor(100000 + Math.random() * 900000)}`;
      const newTicket = await ticketRepository.create({
        ticketCode,
        eventId,
        userId: userId || `guest_${Date.now()}`,
        attendeeName,
        tier,
        pricePaid: event.price,
        status: 'valid',
        wristbandId: null,
        checkInTime: null,
      });
      tickets.push(newTicket);
    }

    return tickets.length === 1 ? tickets[0] : tickets;
  }

  async getTicketById(id) {
    const ticket = await ticketRepository.findById(id);
    if (!ticket) {
      throw ApiError.notFound(`Ticket with ID '${id}' not found`);
    }
    return ticket;
  }

  async getTicketByCode(ticketCode) {
    const ticket = await ticketRepository.findByTicketCode(ticketCode);
    if (!ticket) {
      throw ApiError.notFound(`Ticket with code '${ticketCode}' not found`);
    }
    return ticket;
  }

  async checkInTicket(ticketCode, staffId = null) {
    const ticket = await this.getTicketByCode(ticketCode);

    if (ticket.status === 'checked_in') {
      throw ApiError.conflict(`Ticket ${ticketCode} was already checked in at ${ticket.checkInTime}`);
    }

    if (ticket.status !== 'valid') {
      throw ApiError.badRequest(`Ticket cannot be checked in. Current status: ${ticket.status}`);
    }

    const updated = await ticketRepository.update(ticket.id, {
      status: 'checked_in',
      checkInTime: new Date().toISOString(),
      checkedInByStaffId: staffId,
    });

    return updated;
  }

  async linkWristband(ticketCode, wristbandId) {
    if (!wristbandId) {
      throw ApiError.badRequest('wristbandId is required');
    }

    const ticket = await this.getTicketByCode(ticketCode);

    const existingWithWristband = await ticketRepository.findByWristbandId(wristbandId);
    if (existingWithWristband && existingWithWristband.id !== ticket.id) {
      throw ApiError.conflict(`Wristband ${wristbandId} is already associated with another ticket`);
    }

    const updated = await ticketRepository.update(ticket.id, {
      wristbandId,
      wristbandLinkedAt: new Date().toISOString(),
    });

    return updated;
  }
}

module.exports = new TicketService();
