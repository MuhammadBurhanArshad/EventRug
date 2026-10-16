class ApiResponse {
  static sendSuccess(res, { statusCode = 200, message = 'Success', data = null, meta = null }) {
    const responsePayload = {
      success: true,
      statusCode,
      message,
      data,
    };

    if (meta) {
      responsePayload.meta = meta;
    }

    return res.status(statusCode).json(responsePayload);
  }

  static sendError(res, { statusCode = 500, message = 'An error occurred', errors = null }) {
    const responsePayload = {
      success: false,
      statusCode,
      message,
    };

    if (errors) {
      responsePayload.errors = errors;
    }

    return res.status(statusCode).json(responsePayload);
  }
}

module.exports = ApiResponse;
