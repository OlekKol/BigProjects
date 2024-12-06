const boxes_space = document.querySelector(".boxes")

console.log('dziala')

  for (let i = 0;  i <= 20; i++) {
    const listItem = document.createElement("div");
    listItem.textContent = `box ${i}`;
    
    listItem.style.width = "10vw";
    listItem.style.height = "10vw";
    listItem.style.backgroundColor = "blue";
    listItem.style.fontSize = "20px";
    boxes_space.appendChild(listItem);
  }