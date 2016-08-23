# -*- coding:utf-8 -*-
import re

# match从字符串开头开始匹配，span输出具体的匹配字符串的起始截止位置
print(re.match('www', 'www.baidu.com').span())
print(re.match('com', 'www.baidu.com'))

line = "Cats are smarter than  dogs"

matchObj = re.match('(.*) are (.*) than (.*)', line, re.M | re.I)

if matchObj:
    print "matchObj.group() :", matchObj.group()
    print "matchObj.group(1) :", matchObj.group(1)
    print "matchObj.group(2) :", matchObj.group(2)
    print "matchObj.group(3) :", matchObj.group(3)
else:
    print "No match!!"
    
# match不支持从中间开始匹配
matchObj = re.match('are (.*) than (.*)', line, re.M | re.I)

if matchObj:
    print "matchObj.group() :", matchObj.group()
    print "matchObj.group(1) :", matchObj.group(1)
    print "matchObj.group(2) :", matchObj.group(2)
    print "matchObj.group(3) :", matchObj.group(3)
else:
    print "No match!!"
    
# search从任意地方开始匹配
matchObj = re.search('are (.*) than (.*)', line, re.M | re.I)

if matchObj:
    print "matchObj.group() :", matchObj.group()
    print "matchObj.group(1) :", matchObj.group(1)
    print "matchObj.group(2) :", matchObj.group(2)
else:
    print "No match!!"
    

text = "He was carefully disguised but captured quickly by police."
items = re.findall("(\w+)ly\s(\w+)", text)
print items
    
text = """<div class="article block untagged mb15" id='qiushi_tag_117250539'>

<div class="author clearfix">"""

items = re.findall(r"""<div class="article block untagged mb15" id='qiushi_tag_117250539'>\n\n<div""", text)
print items


pageCode="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">
<title>














24小时爆笑笑话大全 - 糗事百科

</title>

















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时最糗搞笑笑话大全,糗百24小时内最新最糗事就只在糗事百科官网24小时专题,囊括恶搞、最尴尬糗事精华,快乐减压！"/>

<meta http-equiv="mobile-agent" content="format=xhtml;url=http://www.qiushibaike.com/">
<meta http-equiv="mobile-agent" content="format=html5;url=http://www.qiushibaike.com/">




<meta name="robots" content="noarchive">
<link href="http://static.qiushibaike.com/css/dist/web/app.min.css?v=2b259e81b8b4a62a7fe3c19b670facaa" media="screen, projection" rel="stylesheet" type="text/css"/>
<script>
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "//hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
</script>
</head>
<body>

<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/">24小时</a>
<a  href="/imgrank/">图片</a>
<a  href="/text/">文字</a>
<a  href="/history/">穿越</a>
<a  href="/pic/">糗图</a>
<a  href="/textnew/">新鲜</a>
<a  class="fn-signin-required" href="javascript:void(0);" data-go="/add" rel="nofollow">投稿</a>
<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>
<div class="userbar clearfix">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>
</div>
</div>


<div id="content" class="main">
<div class="content-block clearfix">

<div id="content-left" class="col1">





<div class="article block untagged mb15" id='qiushi_tag_117250539'>

<div class="author clearfix">
<a href="/users/12863269/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1286/12863269/medium/20160523174232.jpg" alt="建胃消食"/>
</a>
<a href="/users/12863269/" target="_blank" title="建胃消食">
<h2>建胃消食</h2>
</a>
</div>


<div class="content">

本届奥运会最令我感动的， 不是那些未得奖牌仍然拼搏的运动员， 而是那些双目失明， 依然坚守在工作岗位的裁判们......

</div>




<div class="stats">
<span class="stats-vote"><i class="number">20789</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117250539" data-share="/article/117250539" id="c-117250539" class="qiushi_comments" target="_blank">
<i class="number">285</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117250539" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117250539" class="up">
<a href="javascript:voting(117250539,1)" class="voting" data-article="117250539" id="up-117250539" rel="nofollow">
<i></i>
<span class="number hidden">21186</span>
</a>
</li>
<li id="vote-dn-117250539" class="down">
<a href="javascript:voting(117250539,-1)" class="voting" data-article="117250539" id="dn-117250539" rel="nofollow">
<i></i>
<span class="number hidden">-397</span>
</a>
</li>

<li class="comments">
<a href="/article/117250539" id="c-117250539" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117257915'>

<div class="author clearfix">
<a href="/users/29447394/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2944/29447394/medium/20160122190531.jpg" alt="娜奴娃"/>
</a>
<a href="/users/29447394/" target="_blank" title="娜奴娃">
<h2>娜奴娃</h2>
</a>
</div>


<div class="content">

酒这个东西，能不沾就尽量别沾，刚刚我就亲临了一件酒后暴力事件……<br/><br/>我老婆喝醉了，把我打了一顿……

</div>




<div class="stats">
<span class="stats-vote"><i class="number">5325</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117257915" data-share="/article/117257915" id="c-117257915" class="qiushi_comments" target="_blank">
<i class="number">79</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117257915" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117257915" class="up">
<a href="javascript:voting(117257915,1)" class="voting" data-article="117257915" id="up-117257915" rel="nofollow">
<i></i>
<span class="number hidden">5422</span>
</a>
</li>
<li id="vote-dn-117257915" class="down">
<a href="javascript:voting(117257915,-1)" class="voting" data-article="117257915" id="dn-117257915" rel="nofollow">
<i></i>
<span class="number hidden">-97</span>
</a>
</li>

<li class="comments">
<a href="/article/117257915" id="c-117257915" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117259651'>

<div class="author clearfix">
<a href="/users/13226322/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1322/13226322/medium/20160628202911.jpg" alt="寡人帝辛"/>
</a>
<a href="/users/13226322/" target="_blank" title="寡人帝辛">
<h2>寡人帝辛</h2>
</a>
</div>


<div class="content">

幼儿园快开学了，最近天天嘱咐儿子:“在幼儿园里要听老师的话，和小朋友和睦相处，不要打架，不要丢爸爸妈妈的脸……”儿子“知道了知道了，我又没拿着你们的脸去上学……”

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3898</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117259651" data-share="/article/117259651" id="c-117259651" class="qiushi_comments" target="_blank">
<i class="number">40</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117259651" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117259651" class="up">
<a href="javascript:voting(117259651,1)" class="voting" data-article="117259651" id="up-117259651" rel="nofollow">
<i></i>
<span class="number hidden">3974</span>
</a>
</li>
<li id="vote-dn-117259651" class="down">
<a href="javascript:voting(117259651,-1)" class="voting" data-article="117259651" id="dn-117259651" rel="nofollow">
<i></i>
<span class="number hidden">-76</span>
</a>
</li>

<li class="comments">
<a href="/article/117259651" id="c-117259651" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117251957'>

<div class="author clearfix">
<a href="/users/2362204/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/236/2362204/medium/20160725135123.jpg" alt="一支地西泮"/>
</a>
<a href="/users/2362204/" target="_blank" title="一支地西泮">
<h2>一支地西泮</h2>
</a>
</div>


<div class="content">

我给别人做了一次媒，<br/>一个是我从小玩到大的兄弟，<br/>一个是我高二的女同桌，<br/>也不是拉皮条，<br/>就是觉得他们性格挺像的，<br/>介绍给他们做朋友。<br/><br/>他们都属于那种不会聊天的，<br/>加了qq好友后，<br/>两个人都不知道说什么，<br/>叮咚～<br/>我哥们在qq问我，<br/>“她说你好，我该怎么说啊？”<br/>“你也说你好啊，笨，问她今天学习累不累。”<br/><br/>滴滴滴～<br/>我同桌又给我发消息，<br/>“你朋友问我今天学习累不累，我该怎么回答啊？”<br/>“你告诉他还好，就是做完功课有些无聊。”<br/><br/>滴滴滴～<br/>“你同学说她很无聊，怎么办？”<br/>“那你跟她聊聊喜欢谁的歌。”<br/><br/>滴滴滴～<br/>“他问我喜欢谁的歌，我要说谁？”<br/>“你就说你喜欢周杰伦。”<br/><br/>………………………………………<br/>就这样我跟自己聊了一晚上，<br/>最后他们在一起了，<br/>我有种自己操自己的感觉。

</div>




<div class="stats">
<span class="stats-vote"><i class="number">20022</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117251957" data-share="/article/117251957" id="c-117251957" class="qiushi_comments" target="_blank">
<i class="number">559</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117251957" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117251957" class="up">
<a href="javascript:voting(117251957,1)" class="voting" data-article="117251957" id="up-117251957" rel="nofollow">
<i></i>
<span class="number hidden">20458</span>
</a>
</li>
<li id="vote-dn-117251957" class="down">
<a href="javascript:voting(117251957,-1)" class="voting" data-article="117251957" id="dn-117251957" rel="nofollow">
<i></i>
<span class="number hidden">-436</span>
</a>
</li>

<li class="comments">
<a href="/article/117251957" id="c-117251957" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117248720'>

<div class="author clearfix">
<a href="/users/20541577/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2054/20541577/medium/nopic.jpg" alt="长的帅总被揍！"/>
</a>
<a href="/users/20541577/" target="_blank" title="长的帅总被揍！">
<h2>长的帅总被揍！</h2>
</a>
</div>


<div class="content">

一对情侣在外边吃饭，女生要男生喂她，在这时女生问：“除了我，你还喂过谁”？男生深沉而冷静地回答：“我还喂过狗”。

</div>




<div class="stats">
<span class="stats-vote"><i class="number">11447</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117248720" data-share="/article/117248720" id="c-117248720" class="qiushi_comments" target="_blank">
<i class="number">123</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117248720" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117248720" class="up">
<a href="javascript:voting(117248720,1)" class="voting" data-article="117248720" id="up-117248720" rel="nofollow">
<i></i>
<span class="number hidden">11689</span>
</a>
</li>
<li id="vote-dn-117248720" class="down">
<a href="javascript:voting(117248720,-1)" class="voting" data-article="117248720" id="dn-117248720" rel="nofollow">
<i></i>
<span class="number hidden">-242</span>
</a>
</li>

<li class="comments">
<a href="/article/117248720" id="c-117248720" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117259652'>

<div class="author clearfix">
<a href="/users/31933729/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3193/31933729/medium/20160609221733.jpg" alt="小乔小默"/>
</a>
<a href="/users/31933729/" target="_blank" title="小乔小默">
<h2>小乔小默</h2>
</a>
</div>


<div class="content">

给四岁的儿子买了件带汽车图案的体恤衫，他死活不穿，哭着要奥特曼图案的，实在哄不住了，老公对儿子说，这是奥特曼变身变成汽车了，多酷啊，儿子听完高兴的穿上了……

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1786</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117259652" data-share="/article/117259652" id="c-117259652" class="qiushi_comments" target="_blank">
<i class="number">15</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117259652" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117259652" class="up">
<a href="javascript:voting(117259652,1)" class="voting" data-article="117259652" id="up-117259652" rel="nofollow">
<i></i>
<span class="number hidden">1820</span>
</a>
</li>
<li id="vote-dn-117259652" class="down">
<a href="javascript:voting(117259652,-1)" class="voting" data-article="117259652" id="dn-117259652" rel="nofollow">
<i></i>
<span class="number hidden">-34</span>
</a>
</li>

<li class="comments">
<a href="/article/117259652" id="c-117259652" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117252754'>

<div class="author clearfix">
<a href="/users/32086791/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3208/32086791/medium/2016081301415877.JPEG" alt="萌萌有毒"/>
</a>
<a href="/users/32086791/" target="_blank" title="萌萌有毒">
<h2>萌萌有毒</h2>
</a>
</div>


<div class="content">

买了六个包子<br/>别人老婆：我吃一个就够了。<br/>我老婆：你吃一个就够了吧？

</div>




<div class="stats">
<span class="stats-vote"><i class="number">8132</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117252754" data-share="/article/117252754" id="c-117252754" class="qiushi_comments" target="_blank">
<i class="number">134</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117252754" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117252754" class="up">
<a href="javascript:voting(117252754,1)" class="voting" data-article="117252754" id="up-117252754" rel="nofollow">
<i></i>
<span class="number hidden">8312</span>
</a>
</li>
<li id="vote-dn-117252754" class="down">
<a href="javascript:voting(117252754,-1)" class="voting" data-article="117252754" id="dn-117252754" rel="nofollow">
<i></i>
<span class="number hidden">-180</span>
</a>
</li>

<li class="comments">
<a href="/article/117252754" id="c-117252754" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117258621'>

<div class="author clearfix">
<a href="/users/11177867/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1117/11177867/medium/2016080614155363.JPEG" alt="孟婆卖萌不卖汤、"/>
</a>
<a href="/users/11177867/" target="_blank" title="孟婆卖萌不卖汤、">
<h2>孟婆卖萌不卖汤、</h2>
</a>
</div>


<div class="content">

姐妹儿旅游住旅馆，走的时候让旅馆师傅把她送到安全点的地方下车。于是，她们就在公安局下车了。哈哈哎哎哎……

</div>




<div class="stats">
<span class="stats-vote"><i class="number">4679</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117258621" data-share="/article/117258621" id="c-117258621" class="qiushi_comments" target="_blank">
<i class="number">41</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117258621" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117258621" class="up">
<a href="javascript:voting(117258621,1)" class="voting" data-article="117258621" id="up-117258621" rel="nofollow">
<i></i>
<span class="number hidden">4779</span>
</a>
</li>
<li id="vote-dn-117258621" class="down">
<a href="javascript:voting(117258621,-1)" class="voting" data-article="117258621" id="dn-117258621" rel="nofollow">
<i></i>
<span class="number hidden">-100</span>
</a>
</li>

<li class="comments">
<a href="/article/117258621" id="c-117258621" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117256327'>

<div class="author clearfix">
<a href="/users/25190748/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2519/25190748/medium/201607271844408.JPEG" alt="二女子、"/>
</a>
<a href="/users/25190748/" target="_blank" title="二女子、">
<h2>二女子、</h2>
</a>
</div>


<div class="content">

有个朋友出去鬼混，又被老婆关起门来揍！
他爹急得直跺脚，对他妈说，要不，咱报 警吧，再这样打下去，会出人命的！
他妈说：报毛线警，咱儿媳妇就是警察好吧…

</div>




<div class="stats">
<span class="stats-vote"><i class="number">5791</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117256327" data-share="/article/117256327" id="c-117256327" class="qiushi_comments" target="_blank">
<i class="number">75</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117256327" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117256327" class="up">
<a href="javascript:voting(117256327,1)" class="voting" data-article="117256327" id="up-117256327" rel="nofollow">
<i></i>
<span class="number hidden">5916</span>
</a>
</li>
<li id="vote-dn-117256327" class="down">
<a href="javascript:voting(117256327,-1)" class="voting" data-article="117256327" id="dn-117256327" rel="nofollow">
<i></i>
<span class="number hidden">-125</span>
</a>
</li>

<li class="comments">
<a href="/article/117256327" id="c-117256327" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117257662'>

<div class="author clearfix">
<a href="/users/16749385/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1674/16749385/medium/20160525133512.jpg" alt="王八与蛋"/>
</a>
<a href="/users/16749385/" target="_blank" title="王八与蛋">
<h2>王八与蛋</h2>
</a>
</div>


<div class="content">

邻居家的孩子失恋了，失恋的人往往都爱搞借酒消愁这套。这不邻居家的妈妈又在屋里吼了：“臭小子！你喝这么多干嘛？这酸奶5块多一盒呐！”

</div>




<div class="stats">
<span class="stats-vote"><i class="number">4771</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117257662" data-share="/article/117257662" id="c-117257662" class="qiushi_comments" target="_blank">
<i class="number">44</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117257662" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117257662" class="up">
<a href="javascript:voting(117257662,1)" class="voting" data-article="117257662" id="up-117257662" rel="nofollow">
<i></i>
<span class="number hidden">4874</span>
</a>
</li>
<li id="vote-dn-117257662" class="down">
<a href="javascript:voting(117257662,-1)" class="voting" data-article="117257662" id="dn-117257662" rel="nofollow">
<i></i>
<span class="number hidden">-103</span>
</a>
</li>

<li class="comments">
<a href="/article/117257662" id="c-117257662" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































<style>
.yld-pop {display:block;background:white;padding:18px;margin-bottom:15px;cursor:pointer;font-size: 16px;
line-height: 1.6;color: #63625e;}
.yld-author {margin-bottom:12px;height:40px; position: relative;}
.yld-author img.avater {float:left;margin-right:12px;width:40px;height:40px;border-radius:40px;border: solid 1px #f8f7f7;}
.yld-author .add-v{position:absolute;width: 18px; height: 18px;top:22px;left:25px;display: block;}
.yld-author i {float:right;padding:3px 10px;background:#34b5ff;color:#fff;font-style:normal;}
.yld-author span {line-height:40px;}
.yld-content {clear:both;}
.yld-content ul {padding:0;margin:12px 0;}
.yld-content i { padding: 0 2px;background: #34b5ff;color: #fff;margin-right: 12px;font-style:normal;}
.yld-content strong {font-weight: bold;}
.yld-stats {font-size:small;color:#969696;}
</style>
<a href="http://www.youliaodao.cn/topic/248888" target="_blank" rel="nofollow" class="yld-pop">

<div class="yld-author">
<i>百科</i>
<img class="avater" src="https://o42mv2zdo.qnssl.com/FnWImWwOex3xzvm-qhr08PVregBI" alt="呛呛">
<span>呛呛</span>
<img class="add-v" src="http://static.qiushibaike.com/images/qiushi/yld_v.png?v=b3f66a32b16a49a6dc5eb057df2f7ba4" alt="料主" />
</div>
<div class="yld-content">
<strong>我在泰永电气，双电源的问题可以问我</strong>
<ul>
<li><i>问</i>双电源自动切换开关的CB级跟PC级究竟有什么区别啊？</li>
<li><i>问</i>欧标的电源插座，你们有吗？</li>
<li><i>问</i>双电源主要是做什么么呢</li>
</ul>
</div>
<div class="yld-stats">&#9825; 0 个赞</div>

</a>




<div class="article block untagged mb15" id='qiushi_tag_117258638'>

<div class="author clearfix">
<a href="/users/19417745/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1941/19417745/medium/20150611230253.jpg" alt="外卖小王子"/>
</a>
<a href="/users/19417745/" target="_blank" title="外卖小王子">
<h2>外卖小王子</h2>
</a>
</div>


<div class="content">

曾经很傻很天真：抓着2毛钱，准备去买口香糖吃，一边走一边蹦蹦跳跳甩着手，一毛钱从指缝掉进了草垛堆，找了半天没结果，想着再扔一次，看能掉落在哪，最后我就记得有一个人在草垛旁打滚。

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2393</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117258638" data-share="/article/117258638" id="c-117258638" class="qiushi_comments" target="_blank">
<i class="number">16</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117258638" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117258638" class="up">
<a href="javascript:voting(117258638,1)" class="voting" data-article="117258638" id="up-117258638" rel="nofollow">
<i></i>
<span class="number hidden">2443</span>
</a>
</li>
<li id="vote-dn-117258638" class="down">
<a href="javascript:voting(117258638,-1)" class="voting" data-article="117258638" id="dn-117258638" rel="nofollow">
<i></i>
<span class="number hidden">-50</span>
</a>
</li>

<li class="comments">
<a href="/article/117258638" id="c-117258638" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117259663'>

<div class="author clearfix">
<a href="/users/32019126/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3201/32019126/medium/20160718135727.jpg" alt="蜜mora"/>
</a>
<a href="/users/32019126/" target="_blank" title="蜜mora">
<h2>蜜mora</h2>
</a>
</div>


<div class="content">

出来混都是要还的。。。有只一跑出门就四下撒欢啃花啃草的小狗也是够了，防不胜防。直到今天它无知者无畏的啃了一口仙人掌，呵呵哒！

</div>




<div class="stats">
<span class="stats-vote"><i class="number">2952</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117259663" data-share="/article/117259663" id="c-117259663" class="qiushi_comments" target="_blank">
<i class="number">34</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117259663" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117259663" class="up">
<a href="javascript:voting(117259663,1)" class="voting" data-article="117259663" id="up-117259663" rel="nofollow">
<i></i>
<span class="number hidden">3015</span>
</a>
</li>
<li id="vote-dn-117259663" class="down">
<a href="javascript:voting(117259663,-1)" class="voting" data-article="117259663" id="dn-117259663" rel="nofollow">
<i></i>
<span class="number hidden">-63</span>
</a>
</li>

<li class="comments">
<a href="/article/117259663" id="c-117259663" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117244352'>

<div class="author clearfix">
<a href="/users/11792675/" target="_blank" rel="nofollow">
<img src="http://static.qiushibaike.com/images/thumb/missing.png" alt="当你读完名字就会发现有十五个字"/>
</a>
<a href="/users/11792675/" target="_blank" title="当你读完名字就会发现有十五个字">
<h2>当你读完名字就会发现有十五个字</h2>
</a>
</div>


<div class="content">

中国跳水没意思，进水里一点波澜都没有，你看人家菲律宾，入水时惊涛骇浪，跟野猪跳江似的，看着过瘾

</div>




<div class="stats">
<span class="stats-vote"><i class="number">19773</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117244352" data-share="/article/117244352" id="c-117244352" class="qiushi_comments" target="_blank">
<i class="number">368</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117244352" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117244352" class="up">
<a href="javascript:voting(117244352,1)" class="voting" data-article="117244352" id="up-117244352" rel="nofollow">
<i></i>
<span class="number hidden">20245</span>
</a>
</li>
<li id="vote-dn-117244352" class="down">
<a href="javascript:voting(117244352,-1)" class="voting" data-article="117244352" id="dn-117244352" rel="nofollow">
<i></i>
<span class="number hidden">-472</span>
</a>
</li>

<li class="comments">
<a href="/article/117244352" id="c-117244352" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117259414'>

<div class="author clearfix">
<a href="/users/28985110/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2898/28985110/medium/20150615231213.jpg" alt="打不赢我就投翔"/>
</a>
<a href="/users/28985110/" target="_blank" title="打不赢我就投翔">
<h2>打不赢我就投翔</h2>
</a>
</div>


<div class="content">

一只麻雀误闯进家，抓住后放到鹦鹉笼子里，两只鹦鹉站旁边像看傻子一样看着麻雀在笼子上串下跳了两天，终于有次把食盒跳翻了，两只鹦鹉忍无可忍合伙吧麻雀揍了一顿，世界安静了……

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3830</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117259414" data-share="/article/117259414" id="c-117259414" class="qiushi_comments" target="_blank">
<i class="number">64</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117259414" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117259414" class="up">
<a href="javascript:voting(117259414,1)" class="voting" data-article="117259414" id="up-117259414" rel="nofollow">
<i></i>
<span class="number hidden">3912</span>
</a>
</li>
<li id="vote-dn-117259414" class="down">
<a href="javascript:voting(117259414,-1)" class="voting" data-article="117259414" id="dn-117259414" rel="nofollow">
<i></i>
<span class="number hidden">-82</span>
</a>
</li>

<li class="comments">
<a href="/article/117259414" id="c-117259414" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117258471'>

<div class="author clearfix">
<a href="/users/29314260/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2931/29314260/medium/20160422235031.jpg" alt="(糗名昭著)~贝贝"/>
</a>
<a href="/users/29314260/" target="_blank" title="(糗名昭著)~贝贝">
<h2>(糗名昭著)~贝贝</h2>
</a>
</div>


<div class="content">

和小侄女在家磕瓜子！<br/>小侄女说：好无聊，要不咱俩看谁剥瓜子皮吧，看谁剥的多<br/>比就比，谁怕谁！<br/>然后在我一个不注意，小侄女一把抓起我面前的瓜子仁倒进嘴里……

</div>




<div class="stats">
<span class="stats-vote"><i class="number">4306</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117258471" data-share="/article/117258471" id="c-117258471" class="qiushi_comments" target="_blank">
<i class="number">109</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117258471" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117258471" class="up">
<a href="javascript:voting(117258471,1)" class="voting" data-article="117258471" id="up-117258471" rel="nofollow">
<i></i>
<span class="number hidden">4399</span>
</a>
</li>
<li id="vote-dn-117258471" class="down">
<a href="javascript:voting(117258471,-1)" class="voting" data-article="117258471" id="dn-117258471" rel="nofollow">
<i></i>
<span class="number hidden">-93</span>
</a>
</li>

<li class="comments">
<a href="/article/117258471" id="c-117258471" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117259677'>

<div class="author clearfix">
<a href="/users/28007484/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2800/28007484/medium/20150428225738.jpg" alt="请注册昵称"/>
</a>
<a href="/users/28007484/" target="_blank" title="请注册昵称">
<h2>请注册昵称</h2>
</a>
</div>


<div class="content">

我爸有一次喝多了握着我的手，郑重其事的给了我一张银行卡，告诉我了密码，小声的告诉我里面有80万，让我拿去花。我心想酒后吐真言，看来我果真是个富二代。第二天 我去银行，里面连8毛都没有

</div>




<div class="stats">
<span class="stats-vote"><i class="number">3482</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117259677" data-share="/article/117259677" id="c-117259677" class="qiushi_comments" target="_blank">
<i class="number">71</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117259677" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117259677" class="up">
<a href="javascript:voting(117259677,1)" class="voting" data-article="117259677" id="up-117259677" rel="nofollow">
<i></i>
<span class="number hidden">3558</span>
</a>
</li>
<li id="vote-dn-117259677" class="down">
<a href="javascript:voting(117259677,-1)" class="voting" data-article="117259677" id="dn-117259677" rel="nofollow">
<i></i>
<span class="number hidden">-76</span>
</a>
</li>

<li class="comments">
<a href="/article/117259677" id="c-117259677" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117256397'>

<div class="author clearfix">
<a href="/users/25886566/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2588/25886566/medium/20160314151656.jpg" alt="昭昭白玉堂"/>
</a>
<a href="/users/25886566/" target="_blank" title="昭昭白玉堂">
<h2>昭昭白玉堂</h2>
</a>
</div>


<div class="content">

吃了多年的食堂饭菜，印象中伙食最好的是2013年吧，3块钱一大钵鸡肉。吃了俩月<br/>嗯，我还记得那一年禽流感，还记得老板亲戚是养鸡的。

</div>




<div class="stats">
<span class="stats-vote"><i class="number">4347</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117256397" data-share="/article/117256397" id="c-117256397" class="qiushi_comments" target="_blank">
<i class="number">95</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117256397" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117256397" class="up">
<a href="javascript:voting(117256397,1)" class="voting" data-article="117256397" id="up-117256397" rel="nofollow">
<i></i>
<span class="number hidden">4449</span>
</a>
</li>
<li id="vote-dn-117256397" class="down">
<a href="javascript:voting(117256397,-1)" class="voting" data-article="117256397" id="dn-117256397" rel="nofollow">
<i></i>
<span class="number hidden">-102</span>
</a>
</li>

<li class="comments">
<a href="/article/117256397" id="c-117256397" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117256750'>

<div class="author clearfix">
<a href="/users/13659928/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/1365/13659928/medium/2016081319020296.JPEG" alt="&lt;女监&gt;男监狱长"/>
</a>
<a href="/users/13659928/" target="_blank" title="&lt;女监&gt;男监狱长">
<h2>&lt;女监&gt;男监狱长</h2>
</a>
</div>


<div class="content">

表妹今天去相亲，回来显得很郁闷，我问她怎么回事，他说去的时候他堂弟非要跟着。到了地方，男方也带着他妹妹。我堂弟带走了他妹妹，我却没能带走他

</div>




<div class="stats">
<span class="stats-vote"><i class="number">5970</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117256750" data-share="/article/117256750" id="c-117256750" class="qiushi_comments" target="_blank">
<i class="number">54</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117256750" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117256750" class="up">
<a href="javascript:voting(117256750,1)" class="voting" data-article="117256750" id="up-117256750" rel="nofollow">
<i></i>
<span class="number hidden">6109</span>
</a>
</li>
<li id="vote-dn-117256750" class="down">
<a href="javascript:voting(117256750,-1)" class="voting" data-article="117256750" id="dn-117256750" rel="nofollow">
<i></i>
<span class="number hidden">-139</span>
</a>
</li>

<li class="comments">
<a href="/article/117256750" id="c-117256750" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117251708'>

<div class="author clearfix">
<a href="/users/32222733/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3222/32222733/medium/2016081215530364.JPEG" alt="心碎来不及流泪"/>
</a>
<a href="/users/32222733/" target="_blank" title="心碎来不及流泪">
<h2>心碎来不及流泪</h2>
</a>
</div>


<div class="content">

以前做生意的朋友欠了我8万！一直没有消息！电话打不通！在逃避！就刚刚我带着律师来他家！见了他父母！我拿出了欠条（复印件）！她母亲迅雷不及掩耳盗铃之势撕了、吃了！我和律师懵了！然后我又拿了两张出来！这回他母亲懵了！

</div>




<div class="stats">
<span class="stats-vote"><i class="number">14648</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117251708" data-share="/article/117251708" id="c-117251708" class="qiushi_comments" target="_blank">
<i class="number">457</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117251708" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117251708" class="up">
<a href="javascript:voting(117251708,1)" class="voting" data-article="117251708" id="up-117251708" rel="nofollow">
<i></i>
<span class="number hidden">15011</span>
</a>
</li>
<li id="vote-dn-117251708" class="down">
<a href="javascript:voting(117251708,-1)" class="voting" data-article="117251708" id="dn-117251708" rel="nofollow">
<i></i>
<span class="number hidden">-363</span>
</a>
</li>

<li class="comments">
<a href="/article/117251708" id="c-117251708" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>









<div class="article block untagged mb15" id='qiushi_tag_117257855'>

<div class="author clearfix">
<a href="/users/31410551/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/3141/31410551/medium/2016080314413677.JPEG" alt="万诺"/>
</a>
<a href="/users/31410551/" target="_blank" title="万诺">
<h2>万诺</h2>
</a>
</div>


<div class="content">

朋友酒量不好，两瓶就倒的水平，喝多了腿软，扶她回家，我拉不住她，不小心让她坐地上了。初春地面有点凉，她就坐在地上反复喊，啊啊啊啊啊，好凉，快把我捡起来，我屁股掉地上了！！！

</div>




<div class="stats">
<span class="stats-vote"><i class="number">1908</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/117257855" data-share="/article/117257855" id="c-117257855" class="qiushi_comments" target="_blank">
<i class="number">30</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_117257855" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-117257855" class="up">
<a href="javascript:voting(117257855,1)" class="voting" data-article="117257855" id="up-117257855" rel="nofollow">
<i></i>
<span class="number hidden">1948</span>
</a>
</li>
<li id="vote-dn-117257855" class="down">
<a href="javascript:voting(117257855,-1)" class="voting" data-article="117257855" id="dn-117257855" rel="nofollow">
<i></i>
<span class="number hidden">-40</span>
</a>
</li>

<li class="comments">
<a href="/article/117257855" id="c-117257855" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2?s=4903666" rel="nofollow">
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3?s=4903666" rel="nofollow">
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4?s=4903666" rel="nofollow">
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5?s=4903666" rel="nofollow">
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/35?s=4903666" rel="nofollow">
<span class="page-numbers">
35
</span>
</a>
</li>


<li>
<a href="/hot/page/2?s=4903666" rel="nofollow">
<span class="next">
下一页
</span>
</a>
</li>

</ul>

</div>


<div class="col2">
<div id="sidebar" class="sidebar">
<div class="shopwindow">
<script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "http://p.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script>
</div>
<div class="shopwindow">
<script type="text/javascript">
var cpro_id = "u693365";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>


<div class="sidebar-tutorial clearfix">
<h3>糗百小提示</h3>
<div class="sidebar-tutorial-block">
<div class="sidebar-tutorial-keyboard"></div>
<div class="sidebar-tutorial-text">按 Ctrl+D 键，<br/>把糗事百科加入收藏夹</div>
</div>
</div>
<div class="sidebar-tag clearfix">
<h3>爆笑笑话大全</h3>
<div class="sidebar-tag-block">


<a href="/joke/31584/">搞笑中文名字</a>

<a href="/joke/31585/">日本搞笑动漫名字</a>

<a href="/joke/31598/">11搞笑名字</a>

<a href="/joke/31599/">狼人搞笑名字</a>

<a href="/joke/31652/">洪荒之力是什么意思</a>

<a href="/joke/31653/">洪荒之力图片</a>

<a href="/joke/31654/">洪荒之力是什么力量</a>

<a href="/joke/31655/">洪荒之力搞笑说说</a>

<a href="/joke/31656/">洪荒之力搞笑段子</a>

<a href="/joke/31657/">洪荒之力 段子</a>

<a href="/joke/31658/">世界上搞笑的名字</a>

<a href="/joke/31659/">问道搞笑名字</a>

<a href="/joke/31660/">6个字的搞笑名字</a>

<a href="/joke/31661/">搞笑的收件人名字</a>

<a href="/joke/31662/">五个人的组合名字搞笑</a>

<a href="/joke/31663/">3个字的搞笑名字</a>

<a href="/joke/31664/">搞笑舞蹈串烧名字</a>

<a href="/joke/31665/">搞笑网站名字</a>

<a href="/joke/31666/">5个搞笑名字</a>

<a href="/joke/31667/">搞笑霸气名字</a>


</div>
</div>
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/117255472" title="难的是在于坚持" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117255472/small/app117255472.jpg?imageView2/1/w/146/h/146" alt="难的是在于坚持"></span>
</a>
<a href="/article/117255472" title="难的是在于坚持">
<p>难的是在于坚持</p>
</a>
</li>

<li class="item">
<a href="/article/117256442" title="街上遇一辆大众甲壳虫" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117256442/small/app117256442.jpg?imageView2/1/w/146/h/146" alt="街上遇一辆大众甲壳虫"></span>
</a>
<a href="/article/117256442" title="街上遇一辆大众甲壳虫">
<p>街上遇一辆大众甲壳虫</p>
</a>
</li>

<li class="item">
<a href="/article/117258522" title="老夫最爱盛夏天" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117258522/small/app117258522.jpg?imageView2/1/w/146/h/146" alt="老夫最爱盛夏天"></span>
</a>
<a href="/article/117258522" title="老夫最爱盛夏天">
<p>老夫最爱盛夏天</p>
</a>
</li>

<li class="item">
<a href="/article/117258782" title="有没有通河的" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117258782/small/app117258782.jpg?imageView2/1/w/146/h/146" alt="有没有通河的"></span>
</a>
<a href="/article/117258782" title="有没有通河的">
<p>有没有通河的</p>
</a>
</li>

<li class="item">
<a href="/article/117255652" title="搜狐等着吧" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117255652/small/app117255652.jpg?imageView2/1/w/146/h/146" alt="搜狐等着吧"></span>
</a>
<a href="/article/117255652" title="搜狐等着吧">
<p>搜狐等着吧</p>
</a>
</li>

<li class="item">
<a href="/article/117259721" title="能把生日过到谁也不认识谁你们也是绝了" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117259721/small/app117259721.jpg?imageView2/1/w/146/h/146" alt="能把生日过到谁也不认识谁你们也是绝了"></span>
</a>
<a href="/article/117259721" title="能把生日过到谁也不认识谁你们也是绝了">
<p>能把生日过到谁也不认识谁你们也是绝了</p>
</a>
</li>

<li class="item">
<a href="/article/117258823" title="今天的午餐" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117258823/small/app117258823.jpg?imageView2/1/w/146/h/146" alt="今天的午餐"></span>
</a>
<a href="/article/117258823" title="今天的午餐">
<p>今天的午餐</p>
</a>
</li>

<li class="item">
<a href="/article/117257924" title="你的假期余额不足" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117257924/small/app117257924.jpg?imageView2/1/w/146/h/146" alt="你的假期余额不足"></span>
</a>
<a href="/article/117257924" title="你的假期余额不足">
<p>你的假期余额不足</p>
</a>
</li>

<li class="item">
<a href="/article/117256592" title="临车上用毛巾直接盖头上的降温者" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117256592/small/app117256592.jpg?imageView2/1/w/146/h/146" alt="临车上用毛巾直接盖头上的降温者"></span>
</a>
<a href="/article/117256592" title="临车上用毛巾直接盖头上的降温者">
<p>临车上用毛巾直接盖头上的降温者</p>
</a>
</li>

<li class="item">
<a href="/article/117259167" title="仲基欧巴您这是怎么了" rel="nofollow">
<span><img src="http://pic.qiushibaike.com/system/pictures/11725/117259167/small/app117259167.jpg?imageView2/1/w/146/h/146" alt="仲基欧巴您这是怎么了"></span>
</a>
<a href="/article/117259167" title="仲基欧巴您这是怎么了">
<p>仲基欧巴您这是怎么了</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-tag clearfix">
<h3>热门话题</h3>
<div class="sidebar-tag-block">


<a href="/joke/31592/">搞笑的酒店名字</a>

<a href="/joke/31590/">搞笑骂人名字</a>

<a href="/joke/31589/">热血江湖搞笑名字</a>

<a href="/joke/31586/">搞笑的结义名字</a>

<a href="/joke/23041/">给老师的搞笑留言</a>

<a href="/joke/23040/">简短搞笑留言</a>

<a href="/joke/23038/">给朋友空间搞笑留言</a>

<a href="/joke/22948/">中学生搞笑文章</a>

<a href="/joke/22947/">搞笑粤语文章</a>

<a href="/joke/22944/">搞笑通缉令文章</a>

<a href="/joke/22854/">足球守门员搞笑视频</a>

<a href="/joke/22852/">搞笑足球守门员</a>

<a href="/joke/22818/">搞笑广播操音乐</a>

<a href="/joke/22810/">穿越搞笑广播剧</a>

<a href="/joke/22800/">形容没钱的搞笑句子</a>

<a href="/joke/22796/">搞笑歌曲还钱</a>

<a href="/joke/22720/">外国搞笑综艺节目</a>

<a href="/joke/22714/">搞笑类综艺节目</a>

<a href="/joke/22607/">演艺厅搞笑节目</a>

<a href="/joke/22603/">员工搞笑节目</a>


</div>
</div>


<div class="shopwindow">
<script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "http://p.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script>
</div>
<div class="shopwindow">
<script type="text/javascript">
var cpro_id = "u1101312";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>
</div>
</div>



</div>
</div>


<div class="foot">
<div class="foot-ad">
<script type="text/javascript">
var cpro_id = "u2460383";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</div>
<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="http://about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="http://about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="http://android.myapp.com/android/appdetail.jsp?appid=107431&icfa=15144196000105020000&lmid=2031"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="http://itunes.apple.com/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://shang.qq.com/wpa/qunwpa?idkey=da34d190ca97a0b21d64ebc6f3ab72c076ed35820e629b78fcf9f6a78f7063cd"
target="_blank" rel="external nofollow">
网站反馈群
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>京公网安备11010502026088</span>
</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/session">
<input type="hidden" name="_xsrf" value="2|8df949e1|2dd1b8ca51d8209a566397c08ca3886a|1471099801"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="http://static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="http://static.qiushibaike.com/js/dist/web/app.min.js?v=c6bf820341a79dc26f7d3545990992f7"></script>



<script type="text/javascript">
// Baidu Automatic push content
var bp = document.createElement('script');
bp.src = '//push.zhanzhang.baidu.com/push.js';
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(bp, s);
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-71805417-1', 'auto');
ga('send', 'pageview');
</script>
</body>
</html>

"""

# patternStr = r'<div class="author clearfix">\n\S+\n\S+\n</a>\n\S+\n<h2>(\S+)</h2>\n</a>\n</div>\n\n\n<div class="content">\n\n(\S+)\n\n</div>\n\n\n\n\n<div class="stats">\n<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>'
patternStr = r'<div class="author clearfix">\n<a href="/users/\d+/" target="_blank" rel="nofollow">\n<img src="\S+" \S+\n</a>\n<a href="/users/\d+/" target="_blank" title="\S+">\n<h2>(\S*)</h2>\n</a>\n</div>\n\n\n<div class="content">(\n\n[^\n]+)\n\n</div>\n\n\n\n\n<div class="stats">\n<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>'

pattern = re.compile(patternStr)
items = re.findall(pattern,pageCode)
print items


