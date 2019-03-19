$(function () {
    $('.change_goods').click(function () {
        request_data ={
            'cartid':$(this).attr('data_cardid')

        }

        $.get('/axf/changecartselect/', request_data, function (response) {
            console.log(response)
        })
        $('.change_goods').click(function () {
            var sum = 0
            var price = $(this).parent().prev().text()
            var number = $(this).parent().prev().prev().text()

            sum += number * price
            $('.cart_price_block').html(sum)
        })



    })
})