const eventRepository = require('../repositories/eventRepository');
const ApiError = require('../utils/apiError');

class EventService {
  async getAllEvents(query = {}) {
    let events = await eventRepository.findAll();

    if (query.category) {
      events = events.filter(
        (e) => e.category.toLowerCase() === query.category.toLowerCase()
      );
    }

    if (query.status) {
      events = events.filter((e) => e.status.toLowerCase() === query.status.toLowerCase());
    }

    if (query.search) {
      const term = query.search.toLowerCase();
      events = events.filter(
        (e) =>
          e.title.toLowerCase().includes(term) ||
          e.description.toLowerCase().includes(term) ||
          e.venue.toLowerCase().includes(term)
      );
    }

    return events;
  }

  async getEventById(id) {
    const event = await eventRepository.findById(id);
    if (!event) {
      throw ApiError.notFound(`Event with ID '${id}' not found`);
    }
    return event;
  }

  async createEvent(eventData) {
    const { title, description, venue, category, date, price, totalCapacity } = eventData;

    if (!title || !venue || !date || totalCapacity === undefined) {
      throw ApiError.badRequest('Title, venue, date, and totalCapacity are required fields');
    }

    if (totalCapacity <= 0) {
      throw ApiError.badRequest('Total capacity must be a positive integer');
    }

    if (price !== undefined && price < 0) {
      throw ApiError.badRequest('Price cannot be negative');
    }

    const newEvent = await eventRepository.create({
      title: title.trim(),
      description: description ? description.trim() : '',
      venue: venue.trim(),
      category: category ? category.trim() : 'General',
      organizerId: eventData.organizerId || 'org-default',
      date: new Date(date).toISOString(),
      price: Number(price) || 0,
      totalCapacity: Number(totalCapacity),
      availableCapacity: Number(totalCapacity),
      status: 'published',
    });

    return newEvent;
  }

  async updateEvent(id, updateData) {
    const existing = await this.getEventById(id);

    if (updateData.totalCapacity !== undefined && updateData.totalCapacity <= 0) {
      throw ApiError.badRequest('Total capacity must be greater than zero');
    }

    if (updateData.price !== undefined && updateData.price < 0) {
      throw ApiError.badRequest('Price cannot be negative');
    }

    const updated = await eventRepository.update(id, updateData);
    return updated || existing;
  }

  async deleteEvent(id) {
    await this.getEventById(id);
    await eventRepository.delete(id);
    return { id, deleted: true };
  }
}

module.exports = new EventService();
