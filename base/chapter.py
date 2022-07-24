from django.shortcuts import render





def chapter1(request):
    firstname = 'Way'
    lastname = 'Kuswant'
    name = firstname + " " + lastname
    pertanyaan = 'Hitunglah nilai energi elektron (dalam satuan eV) pada atom hidrogen di kulit ke '

    def q(x):
        return pertanyaan + str(x) + ' !'

    nomor = [
        {'id': 1, 'name': q(1)},
        {'id': 2, 'name': q(2)},
        {'id': 3, 'name': q(3)}]

    context = {'firstname': firstname,
               'lastname': lastname,
               'name': name,
               'nomor': nomor}
    return render(request, 'chapter1.html', context)


def chapter2(request):
    return render(request, 'chapter2.html')