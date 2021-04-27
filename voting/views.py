from django.shortcuts import render, redirect
from .forms import VotingForm
from .models import Vote
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import pandas as pd
from django.core.mail import send_mail

# Create your views here.





def votecast(request):
    if request.method == "POST":
        
        voting_form = VotingForm(request.POST)
        
        if voting_form.is_valid(): 
             
            
             email = voting_form.cleaned_data.get('email')
             incoming_voting_number = voting_form.cleaned_data.get('voting_number')
             president_selection = voting_form.cleaned_data.get('president_selection')
             
             '''
             print('Incoming Number', type(incoming_rotary_number), incoming_rotary_number)
             print('President', type(president_selection), president_selection)
             print('Secretary', type(secretary_selection), secretary_selection)
             print('Email', type(email), email)
             '''
             
             #GETTING THE VOTES
             member_votes_path = os.path.join(settings.MEDIA_ROOT, 'member_votes.csv')
             
             member_votes_df = pd.read_csv(filepath_or_buffer = member_votes_path)
             
             voting_no_list = member_votes_df['Voting_Number'].tolist()
             
             voting_no_list = map(str, voting_no_list)
             
             #votes_column_list = member_votes_df.columns.tolist()
             
             
             
             #GETTING THE MEMBER NUMBERS
             member_no_path = os.path.join(settings.MEDIA_ROOT, 'member_numbers.csv')
             
             member_df = pd.read_csv(filepath_or_buffer = member_no_path)
             
             member_no_list = member_df['Member ID'].tolist() 
             
             print(member_no_list)
             
             member_no_list = map(str, member_no_list)  
             
             if (incoming_voting_number in member_no_list): 
                 
                 
                 #CHECKING OF PERSON ALREADY VOTED
                 if (incoming_voting_number in voting_no_list):
                                      
                     
                     #RENDER ALREADY VOTED MESSAGE 
                     message = 'You have already cast your vote. You cannot vote twice'
              
                     context = {
                                'message' : message,
                            }
                        
                     return render(request, 'message.html', context)
                     
                 else:
                     
                     try:
                         '''
                         #SEND CONFIRMATION EMAIL
                         send_mail(
                                    'VOTING CONFIRMATION',
                                    'This email confirms that your vote has been cast with rotary number, ' +  incoming_voting_number + '.'+
                                     'If you did not cast a vote please contact the returning officer immediately.',
                                    settings.EMAIL_HOST_USER,
                                    [email],
                                    fail_silently = False
                                    )
                         '''
                         
                         
                         vote_list_items = [incoming_voting_number, email, president_selection]      
                         member_votes_df = member_votes_df.append(pd.Series(vote_list_items, index = member_votes_df.columns), ignore_index = True)
                         member_votes_df.to_csv(member_votes_path, index = False)
                         
                     except:                  
                         
                         
                         vote_list_items = [incoming_voting_number, email, president_selection]      
                         member_votes_df = member_votes_df.append(pd.Series(vote_list_items, index = member_votes_df.columns), ignore_index = True)
                         member_votes_df.to_csv(member_votes_path, index = False)
                     
                     #RENDER VOTING COMPLETE
                     message = 'You have successfully cast your vote.'
              
                     context = {
                                'message' : message,
                            }
                        
                     return render(request, 'message.html', context)
                 
             else:
                 print('NOT in list')
                 #RENDER NOT VOTER
                 message = 'You are not a member of this Club, hence you are not eligible to vote.'
          
                 context = {
                            'message' : message,
                        }
                    
                 return render(request, 'message.html', context)
                
                
            
    else:
        voting_form = VotingForm()
        #MESSAGE TO BE DISPLPAYED TO CUSTOMER
        message = 'Input your Voting number, email address and select the candidate you are voting for from the drop down menu.'
          
        context = {
                    'voting_form' : voting_form,
                    'message' : message,
                }
        
        return render(request, 'form_view_club.html', context)



'''
def votecast(request):
    if request.method == "POST":
        
        voting_form = VotingForm(request.POST)
        
        if voting_form.is_valid(): 
            
             incoming_rotary_number = voting_form.cleaned_data.get('rotary_number')
             president_selection = voting_form.cleaned_data.get('president_selection')
             secretary_selection = voting_form.cleaned_data.get('secretary_selection')
             email = voting_form.cleaned_data.get('email')
             
             print('Incoming Number', type(incoming_rotary_number), incoming_rotary_number)
             print('President', type(president_selection), president_selection)
             print('Secretary', type(secretary_selection), secretary_selection)
             print('Email', type(email), email)
             
             
              #GETTING THE VOTES
             rotary_votes_path = os.path.join(settings.MEDIA_ROOT, 'rotary_votes.csv')
             
             rotary_votes_df = pd.read_csv(filepath_or_buffer = rotary_votes_path)
             
             votes_column_list = rotary_votes_df.columns.tolist()
             
             
             
             #GETTING THE ROTARY NUMBERS
             rotary_no_path = os.path.join(settings.MEDIA_ROOT, 'rotary_numbers.csv')
             
             rotary_df = pd.read_csv(filepath_or_buffer = rotary_no_path)
             
             rotary_no_list = rotary_df['Member ID'].tolist() 
             
             print(rotary_no_list)
             
             rotary_no_list = map(str, rotary_no_list)  
             
             if (incoming_rotary_number in rotary_no_list): 
                 
                 
                 try:
                     #ACCESSING THE ROTARY OBJECT TO SEE IF VOTE WAS ALREADY CAST
                     rotary_object  = Vote.objects.get(rotary_number = incoming_rotary_number)
                     
                     #RENDER ALREADY VOTED MESSAGE 
                     message = 'You have already cast your vote. You cannot vote twice'
              
                     context = {
                                'message' : message,
                            }
                        
                     return render(request, 'message.html', context)
                     
                 except:
                     
                     try:
                         #SEND CONFIRMATION EMAIL
                         send_mail(
                                    'VOTING CONFIRMATION',
                                    'This email confirms that your vote has been cast with rotary number, ' +  incoming_rotary_number + '.'+
                                     'If you did not cast a vote please contact the returning officer immediately.',
                                    settings.EMAIL_HOST_USER,
                                    [email],
                                    fail_silently = False
                                    )
                         
                         #SAVING THE VOTED DATA INTO THE DATA BASE
                         Vote(rotary_number = incoming_rotary_number,
                                email = email,
                                president_vote = president_selection,  
                                secretary_vote = secretary_selection).save()
                         
                         vote_list_items = [incoming_rotary_number, email, president_selection, secretary_selection]      
                         rotary_votes_df = rotary_votes_df.append(pd.Series(vote_list_items, index = rotary_votes_df.columns), ignore_index = True)
                         rotary_votes_df.to_csv(rotary_votes_path, index = False)
                         
                     except:                  
                         #SAVING THE VOTED DATA INTO THE DATA BASE
                         Vote(rotary_number = incoming_rotary_number,
                                email = email,
                                president_vote = president_selection,
                                secretary_vote = secretary_selection).save()
                         
                         vote_list_items = [incoming_rotary_number, email, president_selection, secretary_selection]      
                         rotary_votes_df = rotary_votes_df.append(pd.Series(vote_list_items, index = rotary_votes_df.columns), ignore_index = True)
                         rotary_votes_df.to_csv(rotary_votes_path, index = False)
                     
                     #RENDER VOTING COMPLETE
                     message = 'You have successfully cast your vote. Check your mailbox for a confirmation email'
              
                     context = {
                                'message' : message,
                            }
                        
                     return render(request, 'message.html', context)
                 
             else:
                 print('NOT in list')
                 #RENDER NOT VOTER
                 message = 'You are not a member of the Rotary Club of Kampala Seven Hills, hence you are not eligible to vote.'
          
                 context = {
                            'message' : message,
                        }
                    
                 return render(request, 'message.html', context)
                
                
            
    else:
        voting_form = VotingForm()
        #MESSAGE TO BE DISPLPAYED TO CUSTOMER
        message = 'Input your Rotary number, email address and select the candidate you are voting for from the menus.'
          
        context = {
                    'voting_form' : voting_form,
                    'message' : message,
                }
        
        return render(request, 'form_view.html', context)
'''        
    
    
    

    

 