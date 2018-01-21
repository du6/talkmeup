<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- NewPage -->
<html lang="en">
<head>
<!-- Generated by javadoc (1.8.0_151) on Mon Dec 25 12:44:31 EST 2017 -->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>DefaultSDContextGenerator (Apache OpenNLP Tools 1.8.4 API)</title>
<meta name="date" content="2017-12-25">
<link rel="stylesheet" type="text/css" href="../../../stylesheet.css" title="Style">
<script type="text/javascript" src="../../../script.js"></script>
</head>
<body>
<script type="text/javascript"><!--
    try {
        if (location.href.indexOf('is-external=true') == -1) {
            parent.document.title="DefaultSDContextGenerator (Apache OpenNLP Tools 1.8.4 API)";
        }
    }
    catch(err) {
    }
//-->
var methods = {"i0":10};
var tabs = {65535:["t0","All Methods"],2:["t2","Instance Methods"],8:["t4","Concrete Methods"]};
var altColor = "altColor";
var rowColor = "rowColor";
var tableTab = "tableTab";
var activeTableTab = "activeTableTab";
</script>
<noscript>
<div>JavaScript is disabled on your browser.</div>
</noscript>
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="topNav"><a name="navbar.top">
<!--   -->
</a>
<div class="skipNav"><a href="#skip.navbar.top" title="Skip navigation links">Skip navigation links</a></div>
<a name="navbar.top.firstrow">
<!--   -->
</a>
<ul class="navList" title="Navigation">
<li><a href="../../../overview-summary.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="navBarCell1Rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../index-all.html">Index</a></li>
<li><a href="../../../help-doc.html">Help</a></li>
</ul>
</div>
<div class="subNav">
<ul class="navList">
<li><a href="../../../opennlp/tools/sentdetect/DefaultEndOfSentenceScanner.html" title="class in opennlp.tools.sentdetect"><span class="typeNameLink">Prev&nbsp;Class</span></a></li>
<li><a href="../../../opennlp/tools/sentdetect/EmptyLinePreprocessorStream.html" title="class in opennlp.tools.sentdetect"><span class="typeNameLink">Next&nbsp;Class</span></a></li>
</ul>
<ul class="navList">
<li><a href="../../../index.html?opennlp/tools/sentdetect/DefaultSDContextGenerator.html" target="_top">Frames</a></li>
<li><a href="DefaultSDContextGenerator.html" target="_top">No&nbsp;Frames</a></li>
</ul>
<ul class="navList" id="allclasses_navbar_top">
<li><a href="../../../allclasses-noframe.html">All&nbsp;Classes</a></li>
</ul>
<div>
<script type="text/javascript"><!--
  allClassesLink = document.getElementById("allclasses_navbar_top");
  if(window==top) {
    allClassesLink.style.display = "block";
  }
  else {
    allClassesLink.style.display = "none";
  }
  //-->
</script>
</div>
<div>
<ul class="subNavList">
<li>Summary:&nbsp;</li>
<li>Nested&nbsp;|&nbsp;</li>
<li>Field&nbsp;|&nbsp;</li>
<li><a href="#constructor.summary">Constr</a>&nbsp;|&nbsp;</li>
<li><a href="#method.summary">Method</a></li>
</ul>
<ul class="subNavList">
<li>Detail:&nbsp;</li>
<li>Field&nbsp;|&nbsp;</li>
<li><a href="#constructor.detail">Constr</a>&nbsp;|&nbsp;</li>
<li><a href="#method.detail">Method</a></li>
</ul>
</div>
<a name="skip.navbar.top">
<!--   -->
</a></div>
<!-- ========= END OF TOP NAVBAR ========= -->
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="subTitle">opennlp.tools.sentdetect</div>
<h2 title="Class DefaultSDContextGenerator" class="title">Class DefaultSDContextGenerator</h2>
</div>
<div class="contentContainer">
<ul class="inheritance">
<li><a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true" title="class or interface in java.lang">java.lang.Object</a></li>
<li>
<ul class="inheritance">
<li>opennlp.tools.sentdetect.DefaultSDContextGenerator</li>
</ul>
</li>
</ul>
<div class="description">
<ul class="blockList">
<li class="blockList">
<dl>
<dt>All Implemented Interfaces:</dt>
<dd><a href="../../../opennlp/tools/sentdetect/SDContextGenerator.html" title="interface in opennlp.tools.sentdetect">SDContextGenerator</a></dd>
</dl>
<dl>
<dt>Direct Known Subclasses:</dt>
<dd><a href="../../../opennlp/tools/sentdetect/lang/th/SentenceContextGenerator.html" title="class in opennlp.tools.sentdetect.lang.th">SentenceContextGenerator</a></dd>
</dl>
<hr>
<br>
<pre>public class <span class="typeNameLabel">DefaultSDContextGenerator</span>
extends <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true" title="class or interface in java.lang">Object</a>
implements <a href="../../../opennlp/tools/sentdetect/SDContextGenerator.html" title="interface in opennlp.tools.sentdetect">SDContextGenerator</a></pre>
<div class="block">Generate event contexts for maxent decisions for sentence detection.</div>
</li>
</ul>
</div>
<div class="summary">
<ul class="blockList">
<li class="blockList">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<ul class="blockList">
<li class="blockList"><a name="constructor.summary">
<!--   -->
</a>
<h3>Constructor Summary</h3>
<table class="memberSummary" border="0" cellpadding="3" cellspacing="0" summary="Constructor Summary table, listing constructors, and an explanation">
<caption><span>Constructors</span><span class="tabEnd">&nbsp;</span></caption>
<tr>
<th class="colOne" scope="col">Constructor and Description</th>
</tr>
<tr class="altColor">
<td class="colOne"><code><span class="memberNameLink"><a href="../../../opennlp/tools/sentdetect/DefaultSDContextGenerator.html#DefaultSDContextGenerator-char:A-">DefaultSDContextGenerator</a></span>(char[]&nbsp;eosCharacters)</code>
<div class="block">Creates a new <code>SDContextGenerator</code> instance with
 no induced abbreviations.</div>
</td>
</tr>
<tr class="rowColor">
<td class="colOne"><code><span class="memberNameLink"><a href="../../../opennlp/tools/sentdetect/DefaultSDContextGenerator.html#DefaultSDContextGenerator-java.util.Set-char:A-">DefaultSDContextGenerator</a></span>(<a href="http://docs.oracle.com/javase/8/docs/api/java/util/Set.html?is-external=true" title="class or interface in java.util">Set</a>&lt;<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true" title="class or interface in java.lang">String</a>&gt;&nbsp;inducedAbbreviations,
                         char[]&nbsp;eosCharacters)</code>
<div class="block">Creates a new <code>SDContextGenerator</code> instance which uses
 the set of induced abbreviations.</div>
</td>
</tr>
</table>
</li>
</ul>
<!-- ========== METHOD SUMMARY =========== -->
<ul class="blockList">
<li class="blockList"><a name="method.summary">
<!--   -->
</a>
<h3>Method Summary</h3>
<table class="memberSummary" border="0" cellpadding="3" cellspacing="0" summary="Method Summary table, listing methods, and an explanation">
<caption><span id="t0" class="activeTableTab"><span>All Methods</span><span class="tabEnd">&nbsp;</span></span><span id="t2" class="tableTab"><span><a href="javascript:show(2);">Instance Methods</a></span><span class="tabEnd">&nbsp;</span></span><span id="t4" class="tableTab"><span><a href="javascript:show(8);">Concrete Methods</a></span><span class="tabEnd">&nbsp;</span></span></caption>
<tr>
<th class="colFirst" scope="col">Modifier and Type</th>
<th class="colLast" scope="col">Method and Description</th>
</tr>
<tr id="i0" class="altColor">
<td class="colFirst"><code><a href="http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true" title="class or interface in java.lang">String</a>[]</code></td>
<td class="colLast"><code><span class="memberNameLink"><a href="../../../opennlp/tools/sentdetect/DefaultSDContextGenerator.html#getContext-java.lang.CharSequence-int-">getContext</a></span>(<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/CharSequence.html?is-external=true" title="class or interface in java.lang">CharSequence</a>&nbsp;sb,
          int&nbsp;position)</code>
<div class="block">Returns an array of contextual features for the potential sentence boundary at the
 specified position within the specified string buffer.</div>
</td>
</tr>
</table>
<ul class="blockList">
<li class="blockList"><a name="methods.inherited.from.class.java.lang.Object">
<!--   -->
</a>
<h3>Methods inherited from class&nbsp;java.lang.<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true" title="class or interface in java.lang">Object</a></h3>
<code><a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#equals-java.lang.Object-" title="class or interface in java.lang">equals</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#getClass--" title="class or interface in java.lang">getClass</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#hashCode--" title="class or interface in java.lang">hashCode</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notify--" title="class or interface in java.lang">notify</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#notifyAll--" title="class or interface in java.lang">notifyAll</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#toString--" title="class or interface in java.lang">toString</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait--" title="class or interface in java.lang">wait</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long-" title="class or interface in java.lang">wait</a>, <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html?is-external=true#wait-long-int-" title="class or interface in java.lang">wait</a></code></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
<div class="details">
<ul class="blockList">
<li class="blockList">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<ul class="blockList">
<li class="blockList"><a name="constructor.detail">
<!--   -->
</a>
<h3>Constructor Detail</h3>
<a name="DefaultSDContextGenerator-char:A-">
<!--   -->
</a>
<ul class="blockList">
<li class="blockList">
<h4>DefaultSDContextGenerator</h4>
<pre>public&nbsp;DefaultSDContextGenerator(char[]&nbsp;eosCharacters)</pre>
<div class="block">Creates a new <code>SDContextGenerator</code> instance with
 no induced abbreviations.</div>
<dl>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>eosCharacters</code> - </dd>
</dl>
</li>
</ul>
<a name="DefaultSDContextGenerator-java.util.Set-char:A-">
<!--   -->
</a>
<ul class="blockListLast">
<li class="blockList">
<h4>DefaultSDContextGenerator</h4>
<pre>public&nbsp;DefaultSDContextGenerator(<a href="http://docs.oracle.com/javase/8/docs/api/java/util/Set.html?is-external=true" title="class or interface in java.util">Set</a>&lt;<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true" title="class or interface in java.lang">String</a>&gt;&nbsp;inducedAbbreviations,
                                 char[]&nbsp;eosCharacters)</pre>
<div class="block">Creates a new <code>SDContextGenerator</code> instance which uses
 the set of induced abbreviations.</div>
<dl>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>inducedAbbreviations</code> - a <code>Set</code> of Strings
     representing induced abbreviations in the training data.
     Example: &quot;Mr.&quot;</dd>
<dd><code>eosCharacters</code> - </dd>
</dl>
</li>
</ul>
</li>
</ul>
<!-- ============ METHOD DETAIL ========== -->
<ul class="blockList">
<li class="blockList"><a name="method.detail">
<!--   -->
</a>
<h3>Method Detail</h3>
<a name="getContext-java.lang.CharSequence-int-">
<!--   -->
</a>
<ul class="blockListLast">
<li class="blockList">
<h4>getContext</h4>
<pre>public&nbsp;<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true" title="class or interface in java.lang">String</a>[]&nbsp;getContext(<a href="http://docs.oracle.com/javase/8/docs/api/java/lang/CharSequence.html?is-external=true" title="class or interface in java.lang">CharSequence</a>&nbsp;sb,
                           int&nbsp;position)</pre>
<div class="block"><span class="descfrmTypeLabel">Description copied from interface:&nbsp;<code><a href="../../../opennlp/tools/sentdetect/SDContextGenerator.html#getContext-java.lang.CharSequence-int-">SDContextGenerator</a></code></span></div>
<div class="block">Returns an array of contextual features for the potential sentence boundary at the
 specified position within the specified string buffer.</div>
<dl>
<dt><span class="overrideSpecifyLabel">Specified by:</span></dt>
<dd><code><a href="../../../opennlp/tools/sentdetect/SDContextGenerator.html#getContext-java.lang.CharSequence-int-">getContext</a></code>&nbsp;in interface&nbsp;<code><a href="../../../opennlp/tools/sentdetect/SDContextGenerator.html" title="interface in opennlp.tools.sentdetect">SDContextGenerator</a></code></dd>
<dt><span class="paramLabel">Parameters:</span></dt>
<dd><code>sb</code> - The <a href="http://docs.oracle.com/javase/8/docs/api/java/lang/String.html?is-external=true" title="class or interface in java.lang"><code>String</code></a> for which sentences are being determined.</dd>
<dd><code>position</code> - An index into the specified string buffer when a sentence boundary may occur.</dd>
<dt><span class="returnLabel">Returns:</span></dt>
<dd>an array of contextual features for the potential sentence boundary at the
 specified position within the specified string buffer.</dd>
</dl>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>
<!-- ========= END OF CLASS DATA ========= -->
<!-- ======= START OF BOTTOM NAVBAR ====== -->
<div class="bottomNav"><a name="navbar.bottom">
<!--   -->
</a>
<div class="skipNav"><a href="#skip.navbar.bottom" title="Skip navigation links">Skip navigation links</a></div>
<a name="navbar.bottom.firstrow">
<!--   -->
</a>
<ul class="navList" title="Navigation">
<li><a href="../../../overview-summary.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="navBarCell1Rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../index-all.html">Index</a></li>
<li><a href="../../../help-doc.html">Help</a></li>
</ul>
</div>
<div class="subNav">
<ul class="navList">
<li><a href="../../../opennlp/tools/sentdetect/DefaultEndOfSentenceScanner.html" title="class in opennlp.tools.sentdetect"><span class="typeNameLink">Prev&nbsp;Class</span></a></li>
<li><a href="../../../opennlp/tools/sentdetect/EmptyLinePreprocessorStream.html" title="class in opennlp.tools.sentdetect"><span class="typeNameLink">Next&nbsp;Class</span></a></li>
</ul>
<ul class="navList">
<li><a href="../../../index.html?opennlp/tools/sentdetect/DefaultSDContextGenerator.html" target="_top">Frames</a></li>
<li><a href="DefaultSDContextGenerator.html" target="_top">No&nbsp;Frames</a></li>
</ul>
<ul class="navList" id="allclasses_navbar_bottom">
<li><a href="../../../allclasses-noframe.html">All&nbsp;Classes</a></li>
</ul>
<div>
<script type="text/javascript"><!--
  allClassesLink = document.getElementById("allclasses_navbar_bottom");
  if(window==top) {
    allClassesLink.style.display = "block";
  }
  else {
    allClassesLink.style.display = "none";
  }
  //-->
</script>
</div>
<div>
<ul class="subNavList">
<li>Summary:&nbsp;</li>
<li>Nested&nbsp;|&nbsp;</li>
<li>Field&nbsp;|&nbsp;</li>
<li><a href="#constructor.summary">Constr</a>&nbsp;|&nbsp;</li>
<li><a href="#method.summary">Method</a></li>
</ul>
<ul class="subNavList">
<li>Detail:&nbsp;</li>
<li>Field&nbsp;|&nbsp;</li>
<li><a href="#constructor.detail">Constr</a>&nbsp;|&nbsp;</li>
<li><a href="#method.detail">Method</a></li>
</ul>
</div>
<a name="skip.navbar.bottom">
<!--   -->
</a></div>
<!-- ======== END OF BOTTOM NAVBAR ======= -->
<p class="legalCopy"><small>Copyright &#169; 2017 <a href="https://www.apache.org/">The Apache Software Foundation</a>. All rights reserved.</small></p>
</body>
</html>
