const eventService = require('../services/eventService');
const ApiResponse = require('../utils/apiResponse');

class EventController {
  async getEvents(req, res, next) {
    try {
      const { category, status, search } = req.query;
      const events = await eventService.getAllEvents({ category, status, search });
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Events fetched successfully',
        data: events,
        meta: { total: events.length },
      });
    } catch (err) {
      next(err);
    }
  }

  async getEventById(req, res, next) {
    try {
      const { id } = req.params;
      const event = await eventService.getEventById(id);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Event details fetched successfully',
        data: event,
      });
    } catch (err) {
      next(err);
    }
  }

  async createEvent(req, res, next) {
    try {
      const event = await eventService.createEvent(req.body);
      return ApiResponse.sendSuccess(res, {
        statusCode: 201,
        message: 'Event created successfully',
        data: event,
      });
    } catch (err) {
      next(err);
    }
  }

  async updateEvent(req, res, next) {
    try {
      const { id } = req.params;
      const updatedEvent = await eventService.updateEvent(id, req.body);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Event updated successfully',
        data: updatedEvent,
      });
    } catch (err) {
      next(err);
    }
  }

  async deleteEvent(req, res, next) {
    try {
      const { id } = req.params;
      const result = await eventService.deleteEvent(id);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Event deleted successfully',
        data: result,
      });
    } catch (err) {
      next(err);
    }
  }
}

module.exports = new EventController();
