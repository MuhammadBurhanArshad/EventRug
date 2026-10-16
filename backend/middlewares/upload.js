const multer = require('multer');
const path = require('path');
const ApiError = require('../utils/apiError');

// Memory storage keeps file buffers for direct processing or cloud uploading (S3, Cloudinary, etc.)
const storage = multer.memoryStorage();

const fileFilter = (req, file, cb) => {
  const allowedExtensions = ['.jpg', '.jpeg', '.png', '.webp', '.pdf'];
  const ext = path.extname(file.originalname).toLowerCase();

  if (allowedExtensions.includes(ext)) {
    cb(null, true);
  } else {
    cb(
      ApiError.badRequest(
        `Unsupported file format: ${ext}. Allowed formats: ${allowedExtensions.join(', ')}`
      ),
      false
    );
  }
};

const upload = multer({
  storage,
  fileFilter,
  limits: {
    fileSize: 5 * 1024 * 1024, // 5MB limit
  },
});

module.exports = upload;
