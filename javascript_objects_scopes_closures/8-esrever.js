#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (const el of list) {
    result.unshift(el);
  }
  return (result);
};
