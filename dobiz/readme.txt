import requests
import json
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random

# SMS API credentials
smsbazaar_username = 'your_smsbazaar_username'
smsbazaar_password = 'your_smsbazaar_password'
smsbazaar_sender_id = 'your_smsbazaar_sender_id'

def send_otp_to_phone(phone_number, token):
    url = 'https://www.smsbazaar.in/app/smsapi/index.php'
    payload = {
        'uname': smsbazaar_username,
        'password': smsbazaar_password,
        'send': smsbazaar_sender_id,
        'dest': phone_number,
        'msg': f'Your otp is {token}'
    }
    r = requests.get(url, params=payload)
    response = r.text.strip()
    if response == '1000':
        return True
    else:
        return False

def send_otp_to_email(email, token):
    send_mail(
                'Email Verification', 
                f'Your otp is {token}',
                 settings.EMAIL_HOST_USER,
                  [user.email], 
                  fail_silently=False,
                  )

def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=form.cleaned_data.get('email'))
            token = str(random.randint(100000, 999999))
            user.otp = token
            token1 = str(random.randint(100000, 999999))
            user.otp_for_mobile = token1
            user.save()
            request.session['user_email'] = user.email
            request.session['user_phone'] = user.phone
            
            # Send OTP to user's phone
            phone_number = form.cleaned_data.get('phone')
            if phone_number:
                send_otp_to_phone(phone_number, token1)

            
            # Send OTP to user's email
            send_otp_to_email(user.email, token)
            
            messages.success(request, " Verification OTP is being sent on your registered Email and Phone Number")
            return redirect('verify')
        
        #recaptcha stuff
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lfi5U8kAAAAACmKRizYxZh6x7MnB85zUPPZy_-P'
        captchadata={
            'secret':secretkey,
            'response':clientkey
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data= captchadata)
        response = json.loads(r.text)
        verify = response['success']
        print('Your success is:', verify)
    
    return render(request, 'register/signup.html', {'form': form})

def verify(request):
    if request.method == 'POST':
        email_otp = request.POST.get('otp')
        phone_otp = request.POST.get('phone_otp') #entered by user
        email = request.session.get('user_email')
        phone = request.session.get('user_phone')
        if not email_otp or not phone_otp:
            messages.error(request, "Please enter both OTPs")
            return redirect('verify')
        user = User.objects.get(email=email)
        user1 = User.objects.get(phone=phone)
        if user.otp == email_otp and user.phone == phone and user.otp_for_mobile == phone_otp:
            user.is_verified = True
            user.save()
            messages.success(request, "Your account has been verified. Please login to complete your profile.")
            return redirect('auth_login')

        else:
            messages.error(request, "Invalid OTP")
            return redirect('verify')
    return render(request, 'register/verify.html')


from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView


 #Request Paytm to transfer the amount to your Payment by User
    # param_dict = {
    #     'MID':'AwelBN38594741815146',
    #     'ORDER_ID':str(order_id),
    #     'TXN_AMOUNT':str(final_price),
    #     'CUST_ID':order.email,
    #     'INDUSTRY_TYPE':'Retail',
    #     'WEBSITE':'WEBSTAGING',
    #     'CHANNEL_ID':'WEB',
    #     'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest'
    # }
    # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
    # return render(request, 'payment/paytm.html',{'param_dict':param_dict})
# @csrf_exempt
# def handlerequest(request):
#     #Paytm will send you POST request here
#     form = request.POST
#     response_dict = {}
#     checksum = None # initialize checksum variable with None
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     if checksum is not None: # check if checksum is assigned
#         verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#         if verify:
#             if response_dict['RESPCODE'] == '01':
#                 print('order successful')
#             else:
#                 print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'payment/paymentstatus.html', {'response': response_dict})



client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
        amount = int(final_price * 100)
        Print('*****************************')
        print(payment)
        Print('*****************************')
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})
        order.razor_pay_order_id = payment['id']

<script>

  // Find out the cart items from localStorage
  if (localStorage.getItem('cart') == null) {
    var cart = {};
  } else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updatecart(cart);
  }
  $('.cart').click(function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
      cart[idstr] = cart[idstr] + 1;
    }
    else {
      cart[idstr] = 1;
    }
    updatecart(cart);
    

  });
  // to update the cart and adding + and - button there.
  function updatecart(cart) {
  var sum = 0;
  for (var item in cart) {
    sum += cart[item]; // add the quantity of the item to the sum
    document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  // set the cart badge to the total quantity, not just the number of unique items
  document.getElementById('cart').innerHTML = sum;
}

  // If plus or minus button is clicked, change the cart as well as the display value
  $('.divpr').on("click", "button.minus", function () {
    a = this.id.slice(5,);
    cart[a] = Math.max(0, cart[a] - 1);
    document.getElementById('val' + a).innerHTML = cart[a];
    updatecart(cart);
  });

  $('.divpr').on("click", "button.plus", function () {
    a = this.id.slice(4,);
    cart[a] = cart[a] + 1;
    document.getElementById('val' + a).innerHTML = cart[a];
    updatecart(cart);
  });

  $(document).ready(function () {
    $('.share-button').click(function () {
      var shareOptions = $(this).siblings('.share-options');
      if (shareOptions.is(':hidden')) {
        shareOptions.slideDown();
      } else {
        shareOptions.slideUp();
      }
    });
  });
</script>