$(function () {
    $('.change_goods').click(function () {
        request_data ={
            'cartid':$(this).attr('data_cardid')

        }

        $.get('/axf/changecartselect/', request_data, function (response) {
            console.log(response)
        })

        function total() {
            var sum = 0

            $('.cart_pro th').each(function () {
                var $confirm = $(this).find('.change_goods')
                var $content = $(this).find('.cart_pro')

            if ($confirm.find('.glyphicon').length){
                var price = $content.find('.price').attr('data-price')
                var num = $content.find('.num').attr('data-number')

                sum += num * price
            }



            })

            $('.cart_price .p').html(sum)

        }

    })
})