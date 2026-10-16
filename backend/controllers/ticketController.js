const ticketService = require('../services/ticketService');
const ApiResponse = require('../utils/apiResponse');

class TicketController {
  async bookTicket(req, res, next) {
    try {
      const ticket = await ticketService.bookTicket(req.body);
      return ApiResponse.sendSuccess(res, {
        statusCode: 201,
        message: 'Ticket booked successfully',
        data: ticket,
      });
    } catch (err) {
      next(err);
    }
  }

  async getTicketById(req, res, next) {
    try {
      const { id } = req.params;
      const ticket = await ticketService.getTicketById(id);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Ticket fetched successfully',
        data: ticket,
      });
    } catch (err) {
      next(err);
    }
  }

  async getTicketByCode(req, res, next) {
    try {
      const { code } = req.params;
      const ticket = await ticketService.getTicketByCode(code);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Ticket details retrieved successfully',
        data: ticket,
      });
    } catch (err) {
      next(err);
    }
  }

  async checkInTicket(req, res, next) {
    try {
      const { code } = req.params;
      const { staffId } = req.body;
      const updatedTicket = await ticketService.checkInTicket(code, staffId);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Ticket successfully verified and checked in',
        data: updatedTicket,
      });
    } catch (err) {
      next(err);
    }
  }

  async linkWristband(req, res, next) {
    try {
      const { code } = req.params;
      const { wristbandId } = req.body;
      const updatedTicket = await ticketService.linkWristband(code, wristbandId);
      return ApiResponse.sendSuccess(res, {
        statusCode: 200,
        message: 'Wristband linked successfully to ticket',
        data: updatedTicket,
      });
    } catch (err) {
      next(err);
    }
  }
}

module.exports = new TicketController();
