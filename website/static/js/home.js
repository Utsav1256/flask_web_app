// Import the necessary libraries
import { gsap } from "gsap";
import { Splitting } from "splitting";

document.addEventListener("DOMContentLoaded", function () {
  // Initialize Splitting.js
  Splitting();

  // Get an array of the split characters
  const splitTitle = new Splitting({ target: "p" });

  // Create a GSAP timeline
  const tl = gsap.timeline();
  tl.from(
    splitTitle.chars,
    {
      opacity: 0,
      y: 80,
      rotateX: -90,
      stagger: 0.02,
    },
    "<"
  ).to(
    splitTitle.chars,
    {
      opacity: 0,
      y: -80,
      rotateX: 90,
      stagger: 0.02,
    },
    "<1"
  );
});
