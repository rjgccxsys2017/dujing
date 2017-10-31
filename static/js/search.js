
cityareaname=new Array(35);
cityareacode=new Array(35);
function first(preP,preC,VeryHuo,selectP,selectC)
{
a=0;
if (selectP=='01')
{ a=1;tempoption=new Option('安徽','01',false,true); }
else
{ tempoption=new Option('安徽','01'); }
eval('document.'+VeryHuo+'.'+preP+'.options[1]=tempoption;');
cityareacode[0]=new Array('0101','0102','0103');
cityareaname[0]=new Array('黄山','黟县','天柱山');

if (selectP=='02')
{ a=2;tempoption=new Option('杭州','02',false,true); }
else
{ tempoption=new Option('杭州','02'); }
eval('document.'+VeryHuo+'.'+preP+'.options[2]=tempoption;');
cityareacode[1]=new Array('0201','0202','0203');
cityareaname[1]=new Array('西湖','宋城','乌镇');

if (selectP=='03')
{ a=03;tempoption=new Option('云南','03',false,true); }
else
{ tempoption=new Option('云南','03'); }
eval('document.'+VeryHuo+'.'+preP+'.options[03]=tempoption;');
cityareacode[02]=new Array('0301','0302','0303');
cityareaname[02]=new Array('大理','丽江','腾冲');



eval('document.'+VeryHuo+'.'+preP+'.options[a].selected=true;');
cityid=selectP;
if (cityid!='0')
{
b=0;for (i=0;i<cityareaname[cityid-1].length;i++)
{
if (selectC==cityareacode[cityid-1][i])
{b=i+1;tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i],false,true);}
else
tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i]);
eval('document.'+VeryHuo+'.'+preC+'.options[i+1]=tempoption;');
}
eval('document.'+VeryHuo+'.'+preC+'.options[b].selected=true;');
}
}
function selectcityarea(preP,preC,VeryHuo)
{
cityid=eval('document.'+VeryHuo+'.'+preP+'.selectedIndex;');
j=eval('document.'+VeryHuo+'.'+preC+'.length;');
for (i=1;i<j;i++)
{eval('document.'+VeryHuo+'.'+preC+'.options[j-i]=null;')}
if (cityid!="0")
{
for (i=0;i<cityareaname[cityid-1].length;i++)
{
tempoption=new Option(cityareaname[cityid-1][i],cityareacode[cityid-1][i]);
eval('document.'+VeryHuo+'.'+preC+'.options[i+1]=tempoption;');
}
}
}
