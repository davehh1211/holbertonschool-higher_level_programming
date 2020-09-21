#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let m = list.length - 1; m >= 0; m--) {
    newlist.push(list[m]);
  }
  return newlist;
};
