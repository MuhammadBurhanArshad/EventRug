const config = require('../config');
const ApiResponse = require('../utils/apiResponse');

// Centralized error handling middleware
// eslint-disable-next-line no-unused-vars
const errorHandler = (err, req, res, next) => {
  let statusCode = err.statusCode || 500;
  let message = err.message || 'Internal Server Error';

  if (!err.isOperational && statusCode === 500 && config.env === 'production') {
    message = 'Internal Server Error';
  }

  const errors = config.env === 'development' && err.stack ? { stack: err.stack } : null;

  return ApiResponse.sendError(res, {
    statusCode,
    message,
    errors,
  });
};

module.exports = errorHandler;
