$(function () {
    $('.bags').click(function () {
    console.log("tianjia")

    response_data={
        'goodsid': $(this).attr('data_goodsid')
    }


    $.get('/mxw/addcart',response_data,function (response) {
        console.log(response)

        if (response.status == -1){

            window.open('/mxw/login/','_self')
        }
        if (response.status == 1){

            alert('添加购物车成功')
            location='/mxw/cart/'
        }
    })
})
})