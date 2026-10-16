const ApiResponse = require('../utils/apiResponse');
const config = require('../config');

class HealthController {
  getHealth(req, res) {
    return ApiResponse.sendSuccess(res, {
      statusCode: 200,
      message: 'EventRug REST API is healthy and operational',
      data: {
        status: 'UP',
        timestamp: new Date().toISOString(),
        uptimeSeconds: Math.floor(process.uptime()),
        environment: config.env,
        version: '1.0.0',
      },
    });
  }
}

module.exports = new HealthController();
