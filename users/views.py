from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from roomit_app.views import update_scores
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ImageForm, OfferPropertyForm
from .models import PropertyForOffer, Image, Profile

from roomit_app.forms import UpdateRequirementsPForm, UpdateRequirementsRForm
from roomit_app.models import RequirementsR, RequirementsP
from django.views.generic.edit import FormView
from django.views.generic import CreateView, UpdateView, TemplateView

from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Hi {}, welcome to ROOMIT! You can now edit your profile'.format(username))
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('fill_info', new_user)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=user.profile)
    read_only = False

    if request.user.username != username:
        read_only = True

    if request.method == 'POST' and request.user.username == username:
        # if request.user == user:
        print('in if')
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            update_scores(request)
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile', request.user)

    context = {
        'user_profile': user,
        'u_form': u_form,
        'p_form': p_form,
        'read_only': read_only,
    }
    print(f'username:{user.username}\nemail: {user.email}')
    return render(request, 'users/profile.html', context)

@login_required
def info(request, username):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Your personal details have been saved and your profile has been created. You can see your profile and edit it at any time by clicking on the 'profile' tab on the top right of the screen.")
            return render(request, 'users/choose_status.html')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/fill_info.html', context)


@login_required
def create_property_offer_view(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        pOffer_form = OfferPropertyForm(request.POST)
        if pOffer_form.is_valid():
           # check if the property for the current user already exists
            if PropertyForOffer.objects.filter(user_id=user.id).exists():
                # update the existing property instance
                property = PropertyForOffer.objects.get(user_id=user.id)
                pOffer_form = OfferPropertyForm(
                    request.POST, instance=property)
            else:
                # create a new property instance for the user
                property = pOffer_form.save(commit=False)
                property.user_id = user.id
            pOffer_form.save()
            # process images only if they were uploaded
            if request.FILES:
                images = request.FILES.getlist('image')
                for image in images:
                    Image.objects.create(property=property, image=image)
            messages.success(request, "Your property info has been saved")
            update_scores(request)
            # Redirect to the property detail page
            return redirect('requirementsR', request.user)
    else:
        try:
            property = get_object_or_404(PropertyForOffer, user=user)
            pOffer_form = OfferPropertyForm(instance=property)
            image_form = ImageForm()
        except:
            pOffer_form = OfferPropertyForm()
            image_form = ImageForm()

        context = {
            'user_profile': user,
            'pOffer_form': pOffer_form,
            'image_form': image_form,
        }

    return render(request, 'users/property_offer.html', context)


@login_required
def set_status(request):
    user = request.user
    if request.method == 'GET':
        Profile.objects.filter(user = user).update(profile_status= request.GET['status'])
        if request.GET['status'] == 'insert in':
            return redirect('property-offer-create', user)
        else:
            return redirect('requirementsP', user)

@login_required
def display_property_offer(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        pOffer_form = OfferPropertyForm(request.POST)
        if pOffer_form.is_valid():
           # check if the property for the current user already exists
            if PropertyForOffer.objects.filter(user_id=user.id).exists():
                # update the existing property instance
                property = PropertyForOffer.objects.get(user_id=user.id)
                pOffer_form = OfferPropertyForm(request.POST, instance=property)
            else:
                # create a new property instance for the user
                property = pOffer_form.save(commit=False)
                property.user_id = user.id
            pOffer_form.save()
            # process images only if they were uploaded
            if request.FILES:
                images = request.FILES.getlist('image')
                for image in images:
                    Image.objects.create(property=property, image=image)
            messages.success(request, "Your property info has been saved")
            update_scores(request)
            # Redirect to the property detail page
            return redirect('property-offer-display', request.user)
    else:
        property = get_object_or_404(PropertyForOffer, user=user)
        property = OfferPropertyForm(instance=property)
        image_form = ImageForm()
        context = {
                'user_profile': user,
                'property_form': property,
                'image_form': image_form,
            }
        return render(request, 'users\property_offer_display.html', context)


@login_required
def display_property_reqs(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateRequirementsPForm(request.POST)
        if form.is_valid():
           # check if the RequirementsP for the current user already exists
            if RequirementsP.objects.filter(user_id = user.id).exists():
                # update the existing RequirementsP instance
                propertyR = RequirementsP.objects.get(user_id=user.id)
                form = UpdateRequirementsPForm(request.POST, instance=propertyR)
            else:
                # create a new RequirementsP instance for the user
                propertyR = form.save(commit=False)
                propertyR.user_id = user.id
            form.save()
            messages.success(request, "Your property's requirements has been saved")
            update_scores(request)
            # Redirect to the RequirementsP detail page
            return redirect('property-reqs-display', request.user)
    else:
        propertyR = get_object_or_404(RequirementsP, user=user)
        property_form = UpdateRequirementsPForm(instance=propertyR)
        context = {
            'user_profile': user,
            'property_form': property_form,
        }
        return render(request, 'users/property_reqs_display.html', context)

@login_required
def display_roomi_reqs(request, username):
    print('In display-roomi-reqs')
    print(request.method)
    user = User.objects.get(username=username)
    if request.method == 'POST':
        print('In display-roomi-reqs, POST')
        form = UpdateRequirementsRForm(request.POST)
        if form.is_valid():
            print('In display-roomi-reqs, Form Is Valid')
           # check if the RequirementsR for the current user already exists
            if RequirementsR.objects.filter(user_id = user.id).exists():
                print('In display-roomi-reqs, Form Is Exist')
                # update the existing RequirementsR instance
                roomiR = RequirementsR.objects.get(user_id = user.id)
                form = UpdateRequirementsRForm(request.POST, instance=roomiR)
            else:
                print('In display-roomi-reqs, Form Is Not Exist')
                # create a new RequirementsR instance for the user
                roomiR = form.save(commit=False)
                roomiR.user_id = user.id
            form.save()
            messages.success(request, "Your roomi's requirements has been updated")
            update_scores(request)
            # Redirect to the RequirementsRForm detail page
            return redirect('roomi-reqs-display', request.user)
    else:
        print('In display-roomi-reqs, GET')
        roomiR = get_object_or_404(RequirementsR, user=user)
        roomi_form = UpdateRequirementsRForm(instance=roomiR)
        context = {
            'user_profile': user,
            'form': roomi_form,
        }
        return render(request, 'users/roomi_reqs_display.html', context)