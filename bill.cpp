#include<iostream>
using namespace std;
int main()
{char cld;
int units;
double bill,tamt=50.0,sc=0.0;
cout<<"enter coustmer id and units";
cin>>cld>>units;
if(units<=100)
bill=units*0.5;
else
bill=100*0.5+200*0.8+(units-300)*0.9;
if(bill<50)
bill=50;
if(bill>300)
sc=bill*0.15;
tamt=tamt+bill+sc;
cout<<"\n coustmer id-"<<cld
<<"\n units-"<<units<<"\n bill calculated-"<<bill<<"\n surcharge-"<<sc<<"\n amount to pay-"<<tamt;
return 0;
}