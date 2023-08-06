function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  const clone = Array.isArray(obj) ? [] : {};

  Object.keys(obj).forEach((key) => {
    clone[key] = deepClone(obj[key]);
  });

  return clone;
}
