from django import forms

'''
class VotingForm(forms.Form):
    rotary_number = forms.CharField()
    email  = forms.EmailField()
    
    presidential_choices = (
        ('Agatha Mbabazize', 'Agatha Mbabazize'),
        ('Jeremy Mujuni', 'Jeremy Mujuni'),  
        ('Alvin Kabwama(dummy)', 'Alvin Kabwama(dummy)')
    )
    
    president_selection = forms.CharField(widget=forms.RadioSelect(choices=presidential_choices))
    secretary_choices = (
        ('Daphine Mwubaha', 'Daphine Mwubaha'),
        ('Kenneth Muyunga', 'Kenneth Muyunga'),
        ('Rita Akankunda', 'Rita Akankunda'),
        ('Alvin Kabwama(dummy)', 'Alvin Kabwama(dummy)')
    )
    secretary_selection = forms.CharField(widget=forms.RadioSelect(choices=secretary_choices))
    
''' 

  
class VotingForm(forms.Form):
    voting_number = forms.CharField()
    email  = forms.EmailField()
    
    presidential_choices = (
        ('Petra Sansa Tenywa', 'Petra Sansa Tenywa'),
        ('Rachael Ayanga Namiiti', 'Rachael Ayanga Namiiti'),
        ('Amina Mutesi Bazibu', 'Amina Mutesi Bazibu'),
        ('Lydia kunihira Abwooli', 'Lydia kunihira Abwooli'),
        ('Hellen Kasedha  Nalumenya', 'Hellen Kasedha  Nalumenya'),
        ('Dr. Madina Adia Makanga', 'Dr. Madina Adia Makanga'),
        ('Acio Sarah', 'Acio Sarah'),
        ('Jemimah Mirembe Kasadha', 'Jemimah Mirembe Kasadha'),
        ('Hellen Nanteza', 'Hellen Nanteza'),
        ('Christina Nansubuga', 'Christina Nansubuga'),
        ('Patricia Sansa Rujumba', 'Patricia Sansa Rujumba'),
        ('Prossy Sansa Ikaaba', 'Prossy Sansa Ikaaba'),
        ('Josephine Nekesa', 'Josephine Nekesa'),
        ('Aliziki Kaudha', 'Aliziki Kaudha'),
        ('Musiime Bridget', 'Musiime Bridget'),
        ('Hon Veronica Kadoko', 'Hon Veronica Kadoko'),
        ('Lydia Nakadama', 'Lydia Nakadama'),
        ('Olivia Mayengo', 'Olivia Mayengo'),
        ('Namwebya Magaret', 'Namwebya Magaret'),
        ('Gloria Kaguna', 'Gloria Kaguna'),
        ('Mercy Kabuye', 'Mercy Kabuye'),
        ('Annet Musibikha', 'Annet Musibikha'),
        ('Prossy Muzaaya', 'Prossy Muzaaya'),
        ('Annet Magambo', 'Annet Magambo'),
        ('Nanvuma Florence', 'Nanvuma Florence'),
        ('Magaret Nabasirye', 'Magaret Nabasirye'),
        ('Jane Dragon', 'Jane Dragon'),
        ('Kiwala Goretti', 'Kiwala Goretti'),
        ('Gorretti Nasiwa', 'Gorretti Nasiwa'),
        ('Aminah Kako', 'Aminah Kako'),
        ('Mariam Nabasirye', 'Mariam Nabasirye'),
        ('Dorothy Namirimu', 'Dorothy Namirimu'),
        ('Ruth Nambasa', 'Ruth Nambasa'),
        ('Monica Akol', 'Monica Akol'),
        ('Dr. Suzan Nakireka Tumwesigye', 'Dr. Suzan Nakireka Tumwesigye'),
        ('Caroline Ilako', 'Caroline Ilako'),
        ('Juliet Nalunga', 'Juliet Nalunga'),
        ('Lydia Akuwa', 'Lydia Akuwa'),
        ('Dr. Aanyu Kevin', 'Dr. Aanyu Kevin'),
        ('Harriet Atim', 'Harriet Atim'),
        ('Marjorie Ssali', 'Marjorie Ssali'),
        ('Diana Nabuya', 'Diana Nabuya'),
        ('Irene Ataliba', 'Irene Ataliba'),
        ('Annette T', 'Annette T'),
        ('Sylivia Sanyu', 'Sylivia Sanyu'),
        ('Joyce Ataro', 'Joyce Ataro'),
        ('Catherine Alikoba', 'Catherine Alikoba'),
        ('Mary Ajambo', 'Mary Ajambo'),
        ('Lydia Nambubi', 'Lydia Nambubi'),
        ('Rose Namusoke', 'Rose Namusoke'),
        ('Rose Namugwere', 'Rose Namugwere'),
        ('Ann Bagala', 'Ann Bagala'),
        ('Dorah Andezu', 'Dorah Andezu'),
        ('Pelagia Tusiime', 'Pelagia Tusiime'),
        ('Winnie Itamba', 'Winnie Itamba'),
        ('Prossy Magala', 'Prossy Magala'),
        ('Natasha C. Tumwebaze', 'Natasha C. Tumwebaze'),
        ('Suzan Bafumba', 'Suzan Bafumba'),
        ('Julian Tino', 'Julian Tino'),
        ('Rose Namugere', 'Rose Namugere'),
        ('Veronica Owundo', 'Veronica Owundo'),
        ('Prossy Nagayi', 'Prossy Nagayi'),
        ('Mercy Ganda', 'Mercy Ganda'),
        ('Dr. Doreen Kobusingye', 'Dr. Doreen Kobusingye'),
        ('Bamwe Josephine', 'Bamwe Josephine'),
        ('Nangobi Harriet okadapawo', 'Nangobi Harriet okadapawo'),
        ('Hadijah Namisango', 'Hadijah Namisango'),
        ('Tinah Nakimera', 'Tinah Nakimera'),
        ('Mary Kyabanabwe', 'Mary Kyabanabwe')        
    )
    president_selection = forms.CharField(widget=forms.Select(choices=presidential_choices))