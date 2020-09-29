let postPanel = document.querySelector(".Create_Post_Dropdown");
let state = 0;
function CreateDropDownOpen() {
  if (state === 0) {
    postPanel.style.display = "block";
    state++;
  } else {
    postPanel.style.display = "none";
    state--;
  }
}
function CreateDropDownClose() {
  postPanel.syle.display = "none";
  state--;
}
function CreateDropDownExit() {
  postPanel.style.display = "none";
  state--;
}
function PageState() {
  var currentScroll = window.scrollY;
  history.pushState({ position: currentScroll }, "");
}
let ID_Memory = [];
function addToMemory(id) {
  if (!ID_Memory.includes(id)) {
    ID_Memory.push(id);
  }
  history.pushState({ ID_Memory: ID_Memory }, "");
}
function PushData() {
  window.location.href = "/beatbox/post/like/" + history.state.ID_Memory.join();
}
window.onload = PushData;
function addToTempCount(arg, likes) {
  let element = document.getElementById(String(arg));
  let x = element.innerHTML;
  if (likes == Number(x)) {
    newNum = String(Number(x) + 1)
    element.innerHTML = newNum
  }
}