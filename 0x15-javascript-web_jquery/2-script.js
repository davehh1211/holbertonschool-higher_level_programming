#!/usr/bin/node
const $ = window.$;
$(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
