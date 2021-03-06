clear
%% draw the tri-angle plot for diversity of community with fd-transmission disease
load('fre.mat')%.mat file comes from the result of readname_fre.m
dive_aver_fre=mean(dive_mat_fre);
dive_var_fre=var(dive_mat_fre);
dive_std_fre=sqrt(dive_var_fre);
%create a txt file, copy the value of the "dive_aver_fre",paste them into the file and save as "dive_fre.txt"
%create a txt file, copy the value of the "dive_std_fre",paste them into the file and save as "dive_fre_std.txt"
system('py dive_fre.py')

%% draw the tri-angle plot for richness of community with fd-transmission disease
pers_aver_fre=mean(pers_mat_fre);
pers_var_fre=var(pers_mat_fre);
pers_std_fre=sqrt(pers_var_fre);
%create a txt file, copy the value of the "pers_aver_fre",paste them into the file and save as "pers_fre.txt"
%create a txt file, copy the value of the "pers_std_fre",paste them into the file and save as "pers_fre_std.txt"

system('py pers_fre.py')%run the pers_fre.py in matlab; pls make sure your python has alreay
% installed the following library :matplotlib,numpy.

%% draw the tri-angle plot for diversity of community with dd-transmission disease
load('den.mat')%.mat file comes from the result of readname_den.m
dive_aver_den=mean(dive_mat_den);
dive_var_den=var(dive_mat_den);
dive_std_den=sqrt(dive_var_den);
%create a txt file, copy the value of the "dive_aver_den",paste them into the file and save as "dive_den.txt"
%create a txt file, copy the value of the "dive_std_den",paste them into the file and save as "dive_den_std.txt"

system('py dive_den.py')

%% draw the tri-angle plot for richness of community with dd-transmission disease

pers_aver_den=mean(pers_mat_den);
pers_var_den=var(pers_mat_den);
pers_std_den=sqrt(pers_var_den);
%create a txt file, copy the value of the "pers_aver_den",paste them into the file and save as "pers_den.txt"
%create a txt file, copy the value of the "pers_std_den",paste them into the file and save as "pers_den_std.txt"

system('py pers_den.py')


