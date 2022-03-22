import matplotlib.pyplot as plt
import numpy as np
import math
coor_x=[-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,-2,-1.5,-1,-0.5,0,0.5,1,1.5,-1,-0.5,0,0.5,1,1.5,2,0,0.5,1,1.5,2,2.5,1,1.5,2,2.5,3,2,2.5,3,3.5,3,3.5,4,4,4.5,5]
coor_y=[0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,6.062177826,6.92820323,7.794228634,0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,6.062177826,6.92820323,0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,6.062177826,0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,0,0.866025404,1.732050808,2.598076211,3.464101615,0,0.866025404,1.732050808,2.598076211,0,0.866025404,1.732050808,0,0.866025404,0]
plt.figure(figsize=(20, 11.4), dpi=70)
plt.subplot(121)
#size=[0.514216321352813,0.577980352514259,0.638824851616027,0.701568857120231,0.757859990953316,0.805544613803441,0.844373094471176,0.872829884637723,0.893000421621132,0.904811625478300,0.480810925610621,0.546588412697524,0.611606471333512,0.673877937699005,0.730633682514174,0.778752706510140,0.819272934026649,0.849155707724869,0.869384625489219,0.442721772839371,0.511499843940653,0.579575126749922,0.645274036485812,0.700456604427649,0.751197124413048,0.791219353832331,0.821643242418220,0.398907299374667,0.470364827953049,0.542323636232089,0.606517603897234,0.669034592170579,0.716815947387167,0.760704677974794,0.348980437396858,0.421951374321755,0.499360952538086,0.567277290429700,0.630734874018795,0.681301608915500,0.292535378897548,0.374687283241333,0.449435239574090,0.520890446917476,0.585170152192095,0.233028531743815,0.315621118073194,0.397351414489596,0.471053026724745,0.167963823707304,0.252105992322043,0.336443149881228,0.0954255751563851,0.179839524899322,0.0279304567726880]
filename='dive_den.txt'
size = np.loadtxt(filename, delimiter=',',dtype=float)
plt.scatter(coor_x, coor_y, c=size, s=3400,marker='h', label='std of prevalence',cmap='coolwarm')
#plt.plot([-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5],[0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,6.062177826,6.92820323,7.794228634],color='grey', linewidth='2.0', linestyle='--')
#plt.plot(range(-4,6,1),[0,0,0,0,0,0,0,0,0,0],color='grey', linewidth='2.0', linestyle='--')
#plt.plot([0.50,1,1.5,2,2.5,3,3.5,4,4.5,5],[7.79422863405995,6.92820323027551,6.06217782649107,5.19615242270663,4.33012701892219,3.46410161513775,2.59807621135332,1.73205080756888,0.866025403784439,0],color='grey', linewidth='2.0', linestyle='--')
cb=plt.colorbar(orientation="horizontal",shrink=0.7)
cb.ax.tick_params(labelsize=16)
font = {'family' : 'Times New Roman',
	'color'  : 'black',
	'weight' : 'normal',
	'size'   : 16,
	}
cb.set_label('Mean of diversity',fontdict=font)
plt.xticks([])
plt.yticks([])
plt.axis('off')
plt.subplot(122)
#size=[0.0327353850700422,0.0346502964438952,0.0320705852876966,0.0305709191621556,0.0261974915072804,0.0204685023689417,0.0150868278861912,0.0113475416142411,0.00881805533240998,0.00728044863300142,0.0340834535128253,0.0338590380055305,0.0333419845890135,0.0291223845597070,0.0267061402379811,0.0218771035643874,0.0167605414057994,0.0134662160227418,0.0105774244647907,0.0321757702702416,0.0326190379359720,0.0328373566719802,0.0305592007117749,0.0269195524582970,0.0217583041249471,0.0180882560943709,0.0151413471093523,0.0313430576511004,0.0348692082427363,0.0343292545680605,0.0328778153758006,0.0279203031034836,0.0248332240996728,0.0209788000687651,0.0304702461214442,0.0347926955060574,0.0363876041695274,0.0341837489283858,0.0310349645654757,0.0276597764459458,0.0294806296204742,0.0350067554674164,0.0375091139508192,0.0356868182252436,0.0323971330125196,0.0274151529477473,0.0354175797368981,0.0376811808282370,0.0375337565380463,0.0236098425501019,0.0349918216503641,0.0404759349125580,0.0170612725947763,0.0334737037552608,0.000654719410321273]

filename='dive_den_std.txt'
size=np.loadtxt(filename, delimiter=',',dtype=float)
plt.scatter(coor_x, coor_y, c=size, s=3400,marker='h', label='std of prevalence',cmap='YlGnBu')
#plt.plot([-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5],[0,0.866025404,1.732050808,2.598076211,3.464101615,4.330127019,5.196152423,6.062177826,6.92820323,7.794228634],color='grey', linewidth='2.0', linestyle='--')
#plt.plot(range(-4,6,1),[0,0,0,0,0,0,0,0,0,0],color='grey', linewidth='2.0', linestyle='--')
#plt.plot([0.50,1,1.5,2,2.5,3,3.5,4,4.5,5],[7.79422863405995,6.92820323027551,6.06217782649107,5.19615242270663,4.33012701892219,3.46410161513775,2.59807621135332,1.73205080756888,0.866025403784439,0],color='grey', linewidth='2.0', linestyle='--')
plt.xticks([])
plt.yticks([])
cb1=plt.colorbar(orientation="horizontal",shrink=0.7)
cb1.ax.tick_params(labelsize=16)
cb1.set_label('Standard deviation of diversity',fontdict=font)
plt.axis('off')
plt.show()
plt.savefig('./dive_den.jpg')
