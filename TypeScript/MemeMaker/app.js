const canvas = document.querySelector("canvas"); // 캔버스
const ctx = canvas.getContext("2d", { willReadFrequently: true }); // 캔버스 컨텍스트
const file = document.getElementById("file");
const lineWidth = document.getElementById("line-width"); // 브러쉬 굵기
const color = document.getElementById("color"); // 색상
const undo = document.getElementById("undo");
let isPainting = false; // 마우스 클릭 상태

const previousStatus = []; // 되돌리기 기능을 위한 변수
const maxStatusLength = 10; // 최대 저장 개수 10개



/**
 * Setting value to variable
 */
canvas.width = 800;
canvas.height = 800;

//! Canvas가 모두 설정된 이후에 context에 대한 값을 초기화해야 제대로 동작함
//! Canvas의 값이 새로 세팅될 때 마다 ctx도 새롭게 초기화되는 듯 함
ctx.lineWidth = lineWidth.value;
ctx.lineCap = "round";



/**
 * Add EventListener
 ** 마우스로 캔버스에 그림을 그릴 수 있게 감지하는 이벤트  추가
 */

 // 마우스 감지
canvas.addEventListener("mousedown", mousedown);
canvas.addEventListener("mouseup", stopDrawing);
canvas.addEventListener("mouseleave", stopDrawing)
canvas.addEventListener("mousemove", draw);

// 브러쉬 굵기 설정
lineWidth.addEventListener("change", () => ctx.lineWidth = lineWidth.value);

// 색상 설정
color.addEventListener("change", setColor);

// 이미지 선택
file.addEventListener("change", selectFile);

// 되돌리기
undo.addEventListener("click", rollback);




/**
 * Functions
 */

function draw(event) {
    if(isPainting === true){
        const x = event.offsetX;
        const y = event.offsetY;
        ctx.lineTo(x, y);
        ctx.stroke();
        return;
    }
}

function stopDrawing(event) {
    isPainting = false;
    ctx.beginPath();
}


function mousedown(event) {
    saveStatus(event);
    isPainting = true;
    draw(event);
}


function setColor(event) {
    ctx.strokeStyle = event.target.value;
    ctx.fillStyle = event.target.value;
}


function selectFile(event) {
    saveStatus(event);
    const file = event.target.files[0];
    const url = URL.createObjectURL(file);
    const image = new Image();
    image.src = url;
    image.onload = function() {
        ctx.drawImage(image, 0 ,0 , canvas.width, canvas.height)
    };
}


function onSaveClick() {
    const url = canvas.toDataURL();
}


function saveStatus(event) {
    const imageData = ctx.getImageData(0, 0, 800, 800);
    console.log("저장됨")
    if(previousStatus.length >= maxStatusLength){
        previousStatus.shift();
        previousStatus.push(imageData);
    }else{
        previousStatus.push(imageData);
    }
}


function rollback(event) {
    console.log(previousStatus.length);
    ctx.putImageData(previousStatus.pop(), 0, 0);
}