// function toggleComments() {
//   var dots = document.getElementById("dots");
//   var moreText = document.getElementById("more");
//   var btnText = document.getElementById("myBtn");

//   if (dots.style.display === "none") {
//     dots.style.display = "inline";
//     btnText.innerHTML = "Read more";
//     moreText.style.display = "none";
//   } else {
//     dots.style.display = "none";
//     btnText.innerHTML = "Read less";
//     moreText.style.display = "inline";
//   }
// }





// // Function to toggle comments on the server-side
// function toggleComments(petId) {
//   var comments = document.getElementById("comments");
//   if (comments) {
//     comments.classList.toggle("hidden");
//   }
// }


// // Function to handle the click event on the "Show Comments" button
// function handleShowComments() {
//   var showCommentsButtons = document.getElementsByClassName("toggle-comments");
//   Array.from(showCommentsButtons).forEach(function (button) {
//     button.addEventListener("click", function () {
//       var petId = button.dataset.petId;
//       toggleComments(petId);
//     });
//   });
// }

// // Call the function to handle the click event on page load
// document.addEventListener("DOMContentLoaded", function () {
//   handleShowComments();
// });