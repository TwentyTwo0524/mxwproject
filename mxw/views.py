import hashlib
import random
import time

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mxw.models import wheel, User, Goods, Cart


def home(request):
    wheels = wheel.objects.all()
    goods_list = Goods.objects.all()

    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if token:
        user = User.objects.get(pk=userid)

    response_dir = {
        'wheels': wheels,
        'user':user,
        'goods_list': goods_list,
    }

    return render(request,'home/index.html',context=response_dir)


def cart(request):
    # token = request.session.get('token')
    # userid = cache.get(token)
    # user = None
    # if token:
    #     user = User.objects.get(pk=userid)
    #
    # carts = Cart.objects.all()
    # response_dir = {
    #     'carts':carts,
    #     'user': user
    # }
    #
    #
    # return render(request,'cart/cart.html',context=response_dir)
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:  # 有登录才显示
        user = User.objects.get(pk=userid)
        carts = user.cart_set.filter(number__gt=0)

        isall = True
        for cart in carts:
            if not cart.isselect:
                isall = False

        response_dir= {
            'carts': carts,
            'isall': isall,
            'user':user,
        }

        return render(request, 'cart/cart.html', context=response_dir)
    else:  # 未登录不显示
        return render(request, 'login/login.html')


def goods_des(request, productid):
    # goods = Goods.objects.all()
    #
    # token = request.session.get('token')
    # userid = cache.get(token)
    # user = None
    # if token:
    #     user = User.objects.get(pk=userid)
    #
    # response_dir = {
    #     'user': user,
    #     'goods':goods
    # }
    #
    # return render(request, 'goods_des/goods_des.html', context=response_dir)
    token = request.session.get('token')
    userid = cache.get(token)
    goods_list = Goods.objects.filter(pk=productid)
    goods = goods_list.first()
    detail_data = {
        'goods': goods,
        'user': userid,
    }
    user = None
    if token:
        user = User.objects.get(pk=userid)
        detail_data['user'] = user

    return render(request, 'goods_des/goods_des.html', context=detail_data)

# def addcart(request):
#     # 获取token
#     token = request.session.get('token')
#
#     # 响应数据
#     response_data = {}
#
#     # 缓存
#     if token:
#         userid = cache.get(token)
#
#         if userid:  # 已经登录
#             user = User.objects.get(pk=userid)
#             goodsid = request.GET.get('goodsid')
#             goods = Goods.objects.get(pk=goodsid)
#
#             # 商品不存在: 添加新记录
#             # 商品存在: 修改number
#             carts = Cart.objects.filter(user=user).filter(goods=goods)
#             if carts.exists():
#                 cart = carts.first()
#                 cart.number = cart.number + 1
#                 cart.save()
#             else:
#                 cart = Cart()
#                 cart.user = user
#                 cart.goods = goods
#                 cart.number = 1
#                 cart.save()
#
#             response_data['status'] = 1
#             response_data['number'] = cart.number
#             response_data['msg'] = '添加 {} 购物车成功: {}'.format(cart.goods.productlongname, cart.number)
#
#             return JsonResponse(response_data)
#
#     # 未登录
#     # 因为是ajax操作，所以重定向是不可以的!
#     # return redirect('axf:login')
#
#     response_data['status'] = -1
#     response_data['msg'] = '请登录后操作'
#
#     return JsonResponse(response_data)




def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()

def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        users = User.objects.filter(email=email)
        if users.exists():  # 存在
            user = users.first()

            if user.password == generate_password(password):  # 验证通过
                # 更新token
                token = generate_token()

                # 状态保持
                cache.set(token, user.id, 60 * 60 * 24 * 3)

                # 传递客户端
                request.session['token'] = token

                return redirect('mxw:home')
            else:  # 密码错误
                return render(request, 'login/login.html', context={'ps_err': '密码错误'})
        else:  # 不存在
            return render(request, 'login/login.html', context={'user_err': '用户不存在'})

def loginout(request):
    request.session.flush()

    return redirect('mxw:home')

def register(request):
    if request.method == 'GET':
        return render(request, 'register/register.html')
    elif request.method == 'POST':
        # 获取数据
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = generate_password(request.POST.get('password'))


        # 存入数据库
        user = User()
        user.email = email
        user.password = password
        user.name = name
        user.save()

        # 状态保持
        token = generate_token()
        # key-value  >>  token:userid
        cache.set(token, user.id, 60*60*24*3)

        request.session['token'] = token

        return redirect('mxw:home')


def addcart(request):
    token = request.session.get('token')

    respinse_data ={

    }

    if token:
        userid = cache.get(token)

        if userid:
            user = User.objects.get(pk=userid)
            goodsid = request.GET.get('goodsid')
            goods = Goods.objects.get(pk=goodsid)

            carts = Cart.objects.filter(user=user).filter(goods=goods)
            if carts.exists():
                cart = carts.first()
                cart.number = cart.number + 1
                cart.save()
            else:
                cart = Cart()
                cart.user = user
                cart.goods = goods
                cart.number = 1
                cart.save()

            respinse_data['status'] = 1
            respinse_data['msg'] = '添加{}成功:{}'.format(cart.goods.productlongname,cart.number)

            return JsonResponse(respinse_data)

    respinse_data['status'] = -1
    respinse_data['msg'] = '请登录后操作'

    return JsonResponse(respinse_data)


def changecarteslect(request):
    cartid = request.GET.get('cartid')

    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'msg': '状态修改成功',
        'status': 1,
        'isselect': cart.isselect
    }

    return JsonResponse(response_data)




