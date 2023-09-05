from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import KorisnikRegistracijaForma, UserUpdateForm, ProfileUpdateForm

def registracija(request):
    if request.method == 'POST':
        form = KorisnikRegistracijaForma(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Vaš korisnički račun je kreiran, sada se možete prijaviti')
            return redirect('login')
    else:
        form = KorisnikRegistracijaForma()
        
    return render(request, 'korisnici/register.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profil)

        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Vaš korisnički račun je ažuriran!')
            return redirect('profil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'korisnici/profil.html', context)
