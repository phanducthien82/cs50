let counter = 0;
function count(){
    counter++;
    document.querySelector('h1').innerHTML = counter;

    // Kiem tra xem bien dem co la boi so cua 10 {10, 20, 30,....}
    // Su dung ky hieu `` va ${} de truyen bien vao trong chuoi cua javascript
    // if(counter % 10 === 0){
    //     alert(`Count is now ${counter}`);
    // }
}

// Tach ma javascript khoi html. Tuy nhien neu ham duoc goi truoc khi doi tuong duoc tai co the se
// gay ra loi, vi trinh duyet chua xac dinh duoc doi tuong se tac dong len. Mot giai phap de xu ly
// van de nay la them su kien addEventListener hoac dua ma javascript xuong cuoi trang khi tat ca
// cac doi tuong da duoc tai
// Luu y: Khi goi ham thi khong dung ()
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;

    //Su dung ham setInterval de tu dong thuc thi sau 1 khoang thoi gian
    setInterval(count, 1000);
});