function toggleMenu() {
  var dropdownLinks = document.getElementById("grammar-check");
  toggleDisplay(dropdownLinks);

  dropdownLinks = document.getElementById("plagiarism-check");
  toggleDisplay(dropdownLinks);

  dropdownLinks = document.getElementById("text-completion");
  toggleDisplay(dropdownLinks);

  dropdownLinks = document.getElementById("paraphrase");
  toggleDisplay(dropdownLinks);

  dropdownLinks = document.getElementById("menu");
  toggleDisplay(dropdownLinks);

  dropdownLinks = document.getElementById("home");
  toggleDisplay(dropdownLinks);
}

function toggleDisplay(element) {
  if (element.style.display === "none") {
    element.style.display = "block";
  } else {
    element.style.display = "none";
  }
}


// Check if dark mode is enabled in localStorage and apply it
const darkModeEnabled = localStorage.getItem('darkModeEnabled');
if (darkModeEnabled === 'true') {
  document.body.classList.add('dark-mode');
}

function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");

  // Save the dark mode state in localStorage
  const isDarkModeEnabled = element.classList.contains('dark-mode');
  localStorage.setItem('darkModeEnabled', isDarkModeEnabled);
}


function loginProcess() {
  var process = document.getElementById("google");
  process.style.display = "none"
  var process = document.getElementById("process");
  process.style.display = "flex"
}