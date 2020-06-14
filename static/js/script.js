"use strict";
var duration = 0.8;
var delay = 0.3;
var revealText = document.querySelector(".reveal");
var letters = revealText.textContent.split("");
revealText.textContent = "";
var middle = letters.filter(function (e) {
    return e !== " ";
}).length / 2;
revealText.style.width = `${middle * 2 * 75}px`;
letters.forEach(function (letter, i) {
    var span = document.createElement("span");
    span.textContent = letter;
    span.style.animationDelay = delay + (i - middle) * 0.1 + "s";
    span.style.fontSize = `${delay + 50 + (middle - i) * 8}px`;
    span.style.verticalAlign = `bottom`;
    revealText.append(span);
});

var floatTextMenuLinks = document.querySelectorAll(".float-text-menu li a");
floatTextMenuLinks.forEach(function (link) {
    var letters = link.textContent.split("");
    link.textContent = "";
    letters.forEach(function (letter, i) {
        var span = document.createElement("span");
        span.textContent = letter;
        span.style.transitionDelay = i / 20 + "s";
        span.dataset.text = letter;
        link.append(span);
    });
});