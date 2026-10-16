const BaseRepository = require('./baseRepository');

class TicketRepository extends BaseRepository {
  constructor() {
    super([
      {
        id: 'tkt-001',
        ticketCode: 'ER-SONIC-98214',
        eventId: 'event-001',
        userId: 'usr-501',
        attendeeName: 'Alex Mercer',
        tier: 'General Admission',
        pricePaid: 85.0,
        status: 'valid', // valid | checked_in | refunded | cancelled
        wristbandId: null,
        checkInTime: null,
      },
    ]);
  }

  async findByTicketCode(ticketCode) {
    return this.findOne((tkt) => tkt.ticketCode.toUpperCase() === ticketCode.toUpperCase());
  }

  async findByEventId(eventId) {
    return this.items.filter((tkt) => tkt.eventId === eventId);
  }

  async findByUserId(userId) {
    return this.items.filter((tkt) => tkt.userId === userId);
  }

  async findByWristbandId(wristbandId) {
    return this.findOne((tkt) => tkt.wristbandId === wristbandId);
  }
}

module.exports = new TicketRepository();
