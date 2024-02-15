function ACFR() {
    var getThing = document.querySelectorAll(
        '._54k8._52jg._56bs._26vk._2b4n._8yzq._3cqr._8yo0._56bt'
    )
    getThing.forEach(function(value) {
        value.click()
    })
    console.log(
        '%c Code đang chạy, Hãy kéo xuống để tải thêm danh sách lời mời cần tự động hủy',
        'color: blue; font-size: 20px'
    )
}
var loop = setInterval(ACFR, 5000)
