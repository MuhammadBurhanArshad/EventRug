const { validationResult } = require('express-validator');
const ApiResponse = require('../utils/apiResponse');

/**
 * Middleware wrapper for express-validator rule chains.
 * @param {Array} validations - Array of express-validator validation chains
 */
const validate = (validations) => {
  return async (req, res, next) => {
    // Run all validations
    await Promise.all(validations.map((validation) => validation.run(req)));

    const errors = validationResult(req);
    if (errors.isEmpty()) {
      return next();
    }

    const formattedErrors = errors.array().map((err) => ({
      field: err.path || err.param,
      message: err.msg,
      value: err.value,
    }));

    return ApiResponse.sendError(res, {
      statusCode: 400,
      message: 'Validation failed',
      errors: formattedErrors,
    });
  };
};

module.exports = validate;
