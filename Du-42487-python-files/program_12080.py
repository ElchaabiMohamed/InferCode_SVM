<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<!-- saved from url=(0063)https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html -->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="generator" content="AsciiDoc 8.6.9">
<title>CA177 — Lab Sheet 5 - ca177</title>
<style type="text/css">
/* Shared CSS for AsciiDoc xhtml11 and html5 backends */

/* Default font. */
body {
  font-family: Georgia,serif;
}

/* Title font. */
h1, h2, h3, h4, h5, h6,
div.title, caption.title,
thead, p.table.header,
#toctitle,
#author, #revnumber, #revdate, #revremark,
#footer {
  font-family: Arial,Helvetica,sans-serif;
}

body {
  margin: 1em 5% 1em 5%;
}

a {
  color: blue;
  text-decoration: underline;
}
a:visited {
  color: fuchsia;
}

em {
  font-style: italic;
  color: navy;
}

strong {
  font-weight: bold;
  color: #083194;
}

h1, h2, h3, h4, h5, h6 {
  color: #527bbd;
  margin-top: 1.2em;
  margin-bottom: 0.5em;
  line-height: 1.3;
}

h1, h2, h3 {
  border-bottom: 2px solid silver;
}
h2 {
  padding-top: 0.5em;
}
h3 {
  float: left;
}
h3 + * {
  clear: left;
}
h5 {
  font-size: 1.0em;
}

div.sectionbody {
  margin-left: 0;
}

hr {
  border: 1px solid silver;
}

p {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}

ul, ol, li > p {
  margin-top: 0;
}
ul > li     { color: #aaa; }
ul > li > * { color: black; }

.monospaced, code, pre {
  font-family: "Courier New", Courier, monospace;
  font-size: inherit;
  color: navy;
  padding: 0;
  margin: 0;
}
pre {
  white-space: pre-wrap;
}

#author {
  color: #527bbd;
  font-weight: bold;
  font-size: 1.1em;
}
#email {
}
#revnumber, #revdate, #revremark {
}

#footer {
  font-size: small;
  border-top: 2px solid silver;
  padding-top: 0.5em;
  margin-top: 4.0em;
}
#footer-text {
  float: left;
  padding-bottom: 0.5em;
}
#footer-badges {
  float: right;
  padding-bottom: 0.5em;
}

#preamble {
  margin-top: 1.5em;
  margin-bottom: 1.5em;
}
div.imageblock, div.exampleblock, div.verseblock,
div.quoteblock, div.literalblock, div.listingblock, div.sidebarblock,
div.admonitionblock {
  margin-top: 1.0em;
  margin-bottom: 1.5em;
}
div.admonitionblock {
  margin-top: 2.0em;
  margin-bottom: 2.0em;
  margin-right: 10%;
  color: #606060;
}

div.content { /* Block element content. */
  padding: 0;
}

/* Block element titles. */
div.title, caption.title {
  color: #527bbd;
  font-weight: bold;
  text-align: left;
  margin-top: 1.0em;
  margin-bottom: 0.5em;
}
div.title + * {
  margin-top: 0;
}

td div.title:first-child {
  margin-top: 0.0em;
}
div.content div.title:first-child {
  margin-top: 0.0em;
}
div.content + div.title {
  margin-top: 0.0em;
}

div.sidebarblock > div.content {
  background: #ffffee;
  border: 1px solid #dddddd;
  border-left: 4px solid #f0f0f0;
  padding: 0.5em;
}

div.listingblock > div.content {
  border: 1px solid #dddddd;
  border-left: 5px solid #f0f0f0;
  background: #f8f8f8;
  padding: 0.5em;
}

div.quoteblock, div.verseblock {
  padding-left: 1.0em;
  margin-left: 1.0em;
  margin-right: 10%;
  border-left: 5px solid #f0f0f0;
  color: #888;
}

div.quoteblock > div.attribution {
  padding-top: 0.5em;
  text-align: right;
}

div.verseblock > pre.content {
  font-family: inherit;
  font-size: inherit;
}
div.verseblock > div.attribution {
  padding-top: 0.75em;
  text-align: left;
}
/* DEPRECATED: Pre version 8.2.7 verse style literal block. */
div.verseblock + div.attribution {
  text-align: left;
}

div.admonitionblock .icon {
  vertical-align: top;
  font-size: 1.1em;
  font-weight: bold;
  text-decoration: underline;
  color: #527bbd;
  padding-right: 0.5em;
}
div.admonitionblock td.content {
  padding-left: 0.5em;
  border-left: 3px solid #dddddd;
}

div.exampleblock > div.content {
  border-left: 3px solid #dddddd;
  padding-left: 0.5em;
}

div.imageblock div.content { padding-left: 0; }
span.image img { border-style: none; vertical-align: text-bottom; }
a.image:visited { color: white; }

dl {
  margin-top: 0.8em;
  margin-bottom: 0.8em;
}
dt {
  margin-top: 0.5em;
  margin-bottom: 0;
  font-style: normal;
  color: navy;
}
dd > *:first-child {
  margin-top: 0.1em;
}

ul, ol {
    list-style-position: outside;
}
ol.arabic {
  list-style-type: decimal;
}
ol.loweralpha {
  list-style-type: lower-alpha;
}
ol.upperalpha {
  list-style-type: upper-alpha;
}
ol.lowerroman {
  list-style-type: lower-roman;
}
ol.upperroman {
  list-style-type: upper-roman;
}

div.compact ul, div.compact ol,
div.compact p, div.compact p,
div.compact div, div.compact div {
  margin-top: 0.1em;
  margin-bottom: 0.1em;
}

tfoot {
  font-weight: bold;
}
td > div.verse {
  white-space: pre;
}

div.hdlist {
  margin-top: 0.8em;
  margin-bottom: 0.8em;
}
div.hdlist tr {
  padding-bottom: 15px;
}
dt.hdlist1.strong, td.hdlist1.strong {
  font-weight: bold;
}
td.hdlist1 {
  vertical-align: top;
  font-style: normal;
  padding-right: 0.8em;
  color: navy;
}
td.hdlist2 {
  vertical-align: top;
}
div.hdlist.compact tr {
  margin: 0;
  padding-bottom: 0;
}

.comment {
  background: yellow;
}

.footnote, .footnoteref {
  font-size: 0.8em;
}

span.footnote, span.footnoteref {
  vertical-align: super;
}

#footnotes {
  margin: 20px 0 20px 0;
  padding: 7px 0 0 0;
}

#footnotes div.footnote {
  margin: 0 0 5px 0;
}

#footnotes hr {
  border: none;
  border-top: 1px solid silver;
  height: 1px;
  text-align: left;
  margin-left: 0;
  width: 20%;
  min-width: 100px;
}

div.colist td {
  padding-right: 0.5em;
  padding-bottom: 0.3em;
  vertical-align: top;
}
div.colist td img {
  margin-top: 0.3em;
}

@media print {
  #footer-badges { display: none; }
}

#toc {
  margin-bottom: 2.5em;
}

#toctitle {
  color: #527bbd;
  font-size: 1.1em;
  font-weight: bold;
  margin-top: 1.0em;
  margin-bottom: 0.1em;
}

div.toclevel0, div.toclevel1, div.toclevel2, div.toclevel3, div.toclevel4 {
  margin-top: 0;
  margin-bottom: 0;
}
div.toclevel2 {
  margin-left: 2em;
  font-size: 0.9em;
}
div.toclevel3 {
  margin-left: 4em;
  font-size: 0.9em;
}
div.toclevel4 {
  margin-left: 6em;
  font-size: 0.9em;
}

span.aqua { color: aqua; }
span.black { color: black; }
span.blue { color: blue; }
span.fuchsia { color: fuchsia; }
span.gray { color: gray; }
span.green { color: green; }
span.lime { color: lime; }
span.maroon { color: maroon; }
span.navy { color: navy; }
span.olive { color: olive; }
span.purple { color: purple; }
span.red { color: red; }
span.silver { color: silver; }
span.teal { color: teal; }
span.white { color: white; }
span.yellow { color: yellow; }

span.aqua-background { background: aqua; }
span.black-background { background: black; }
span.blue-background { background: blue; }
span.fuchsia-background { background: fuchsia; }
span.gray-background { background: gray; }
span.green-background { background: green; }
span.lime-background { background: lime; }
span.maroon-background { background: maroon; }
span.navy-background { background: navy; }
span.olive-background { background: olive; }
span.purple-background { background: purple; }
span.red-background { background: red; }
span.silver-background { background: silver; }
span.teal-background { background: teal; }
span.white-background { background: white; }
span.yellow-background { background: yellow; }

span.big { font-size: 2em; }
span.small { font-size: 0.6em; }

span.underline { text-decoration: underline; }
span.overline { text-decoration: overline; }
span.line-through { text-decoration: line-through; }

div.unbreakable { page-break-inside: avoid; }


/*
 * xhtml11 specific
 *
 * */

div.tableblock {
  margin-top: 1.0em;
  margin-bottom: 1.5em;
}
div.tableblock > table {
  border: 3px solid #527bbd;
}
thead, p.table.header {
  font-weight: bold;
  color: #527bbd;
}
p.table {
  margin-top: 0;
}
/* Because the table frame attribute is overriden by CSS in most browsers. */
div.tableblock > table[frame="void"] {
  border-style: none;
}
div.tableblock > table[frame="hsides"] {
  border-left-style: none;
  border-right-style: none;
}
div.tableblock > table[frame="vsides"] {
  border-top-style: none;
  border-bottom-style: none;
}


/*
 * html5 specific
 *
 * */

table.tableblock {
  margin-top: 1.0em;
  margin-bottom: 1.5em;
}
thead, p.tableblock.header {
  font-weight: bold;
  color: #527bbd;
}
p.tableblock {
  margin-top: 0;
}
table.tableblock {
  border-width: 3px;
  border-spacing: 0px;
  border-style: solid;
  border-color: #527bbd;
  border-collapse: collapse;
}
th.tableblock, td.tableblock {
  border-width: 1px;
  padding: 4px;
  border-style: solid;
  border-color: #527bbd;
}

table.tableblock.frame-topbot {
  border-left-style: hidden;
  border-right-style: hidden;
}
table.tableblock.frame-sides {
  border-top-style: hidden;
  border-bottom-style: hidden;
}
table.tableblock.frame-none {
  border-style: hidden;
}

th.tableblock.halign-left, td.tableblock.halign-left {
  text-align: left;
}
th.tableblock.halign-center, td.tableblock.halign-center {
  text-align: center;
}
th.tableblock.halign-right, td.tableblock.halign-right {
  text-align: right;
}

th.tableblock.valign-top, td.tableblock.valign-top {
  vertical-align: top;
}
th.tableblock.valign-middle, td.tableblock.valign-middle {
  vertical-align: middle;
}
th.tableblock.valign-bottom, td.tableblock.valign-bottom {
  vertical-align: bottom;
}


/*
 * manpage specific
 *
 * */

body.manpage h1 {
  padding-top: 0.5em;
  padding-bottom: 0.5em;
  border-top: 2px solid silver;
  border-bottom: 2px solid silver;
}
body.manpage h2 {
  border-style: none;
}
body.manpage div.sectionbody {
  margin-left: 3em;
}

@media print {
  body.manpage div#toc { display: none; }
}
/* Steve Blott - Slidy with sans serif fonts */

body
{
  /* font-family: "Gill Sans MT", "Gill Sans", GillSans, sans-serif; */
  /* font-family: Arial, Helvetica, sans-serif; */
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}

div.sectionbody
{
  /* font-family: "Gill Sans MT", "Gill Sans", GillSans, sans-serif; */
  /* font-family: Arial, Helvetica, sans-serif; */
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
}

.monospaced, code, pre {
  color: #2F4F4F;
}

p > code {
  font-size: 1.1em;
}

em {
  font-style: italic;
  color: inherit;
}

strong {
  font-weight: bold;
  color: inherit;
}

/*
.code {
  font-size: 1.2em;
}
*/

div.sidebarblock > div.content {
   background-color: #eeeeee;
   border-left-color: #c0c0c0;
   border-top-color: #d0d0d0;
   border-bottom-color: #d0d0d0;
   border-right-color: #d0d0d0;
}

div.listingblock > div.content {
   border-left-width: 3px;
   border-left-color: #c0c0c0;
   border-top-color: #d0d0d0;
   border-bottom-color: #d0d0d0;
   border-right-color: #d0d0d0;
}

body.smblott-mobile {
   /* background-color: lightblue; */
   margin-left: 1em !important;
   margin-right: 1em !important;
   max-width: calc(100% - 2em) !important;
}
#toc.smblott-mobile {
   position: static;
   border-right: 0px;
   display: none;
}

/* Unfortunately, this duplicates the styles above. */
@media screen and (max-width: 900px) {
   body {
      /* background-color: lightblue; */
      margin-left: 1em !important;
      margin-right: 1em !important;
      max-width: calc(100% - 2em) !important;
   }
   #toc {
      position: static;
      border-right: 0px;
      display: none;
   }
}


@media screen {
  body {
    max-width: 50em; /* approximately 80 characters wide */
    margin-left: 16em;
  }

  #toc {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    width: 13em;
    padding: 0.5em;
    padding-bottom: 1.5em;
    margin: 0;
    overflow: auto;
    border-right: 3px solid #f8f8f8;
    background-color: white;
  }

  #toc .toclevel1 {
    margin-top: 0.5em;
  }

  #toc .toclevel2 {
    margin-top: 0.25em;
    display: list-item;
    color: #aaaaaa;
  }

  #toctitle {
    margin-top: 0.5em;
  }
}
</style>
<script type="text/javascript">
/*<![CDATA[*/
var asciidoc = {  // Namespace.

/////////////////////////////////////////////////////////////////////
// Table Of Contents generator
/////////////////////////////////////////////////////////////////////

/* Author: Mihai Bazon, September 2002
 * http://students.infoiasi.ro/~mishoo
 *
 * Table Of Content generator
 * Version: 0.4
 *
 * Feel free to use this script under the terms of the GNU General Public
 * License, as long as you do not remove or alter this notice.
 */

 /* modified by Troy D. Hanson, September 2006. License: GPL */
 /* modified by Stuart Rackham, 2006, 2009. License: GPL */

// toclevels = 1..4.
toc: function (toclevels) {

  function getText(el) {
    var text = "";
    for (var i = el.firstChild; i != null; i = i.nextSibling) {
      if (i.nodeType == 3 /* Node.TEXT_NODE */) // IE doesn't speak constants.
        text += i.data;
      else if (i.firstChild != null)
        text += getText(i);
    }
    return text;
  }

  function TocEntry(el, text, toclevel) {
    this.element = el;
    this.text = text;
    this.toclevel = toclevel;
  }

  function tocEntries(el, toclevels) {
    var result = new Array;
    var re = new RegExp('[hH]([1-'+(toclevels+1)+'])');
    // Function that scans the DOM tree for header elements (the DOM2
    // nodeIterator API would be a better technique but not supported by all
    // browsers).
    var iterate = function (el) {
      for (var i = el.firstChild; i != null; i = i.nextSibling) {
        if (i.nodeType == 1 /* Node.ELEMENT_NODE */) {
          var mo = re.exec(i.tagName);
          if (mo && (i.getAttribute("class") || i.getAttribute("className")) != "float") {
            result[result.length] = new TocEntry(i, getText(i), mo[1]-1);
          }
          iterate(i);
        }
      }
    }
    iterate(el);
    return result;
  }

  var toc = document.getElementById("toc");
  if (!toc) {
    return;
  }

  // Delete existing TOC entries in case we're reloading the TOC.
  var tocEntriesToRemove = [];
  var i;
  for (i = 0; i < toc.childNodes.length; i++) {
    var entry = toc.childNodes[i];
    if (entry.nodeName.toLowerCase() == 'div'
     && entry.getAttribute("class")
     && entry.getAttribute("class").match(/^toclevel/))
      tocEntriesToRemove.push(entry);
  }
  for (i = 0; i < tocEntriesToRemove.length; i++) {
    toc.removeChild(tocEntriesToRemove[i]);
  }

  // Rebuild TOC entries.
  var entries = tocEntries(document.getElementById("content"), toclevels);
  for (var i = 0; i < entries.length; ++i) {
    var entry = entries[i];
    if (entry.element.id == "")
      entry.element.id = "_toc_" + i;
    var a = document.createElement("a");
    a.href = "#" + entry.element.id;
    a.appendChild(document.createTextNode(entry.text));
    var div = document.createElement("div");
    div.appendChild(a);
    div.className = "toclevel" + entry.toclevel;
    toc.appendChild(div);
  }
  if (entries.length == 0)
    toc.parentNode.removeChild(toc);
},


/////////////////////////////////////////////////////////////////////
// Footnotes generator
/////////////////////////////////////////////////////////////////////

/* Based on footnote generation code from:
 * http://www.brandspankingnew.net/archive/2005/07/format_footnote.html
 */

footnotes: function () {
  // Delete existing footnote entries in case we're reloading the footnodes.
  var i;
  var noteholder = document.getElementById("footnotes");
  if (!noteholder) {
    return;
  }
  var entriesToRemove = [];
  for (i = 0; i < noteholder.childNodes.length; i++) {
    var entry = noteholder.childNodes[i];
    if (entry.nodeName.toLowerCase() == 'div' && entry.getAttribute("class") == "footnote")
      entriesToRemove.push(entry);
  }
  for (i = 0; i < entriesToRemove.length; i++) {
    noteholder.removeChild(entriesToRemove[i]);
  }

  // Rebuild footnote entries.
  var cont = document.getElementById("content");
  var spans = cont.getElementsByTagName("span");
  var refs = {};
  var n = 0;
  for (i=0; i<spans.length; i++) {
    if (spans[i].className == "footnote") {
      n++;
      var note = spans[i].getAttribute("data-note");
      if (!note) {
        // Use [\s\S] in place of . so multi-line matches work.
        // Because JavaScript has no s (dotall) regex flag.
        note = spans[i].innerHTML.match(/\s*\[([\s\S]*)]\s*/)[1];
        spans[i].innerHTML =
          "[<a id='_footnoteref_" + n + "' href='#_footnote_" + n +
          "' title='View footnote' class='footnote'>" + n + "</a>]";
        spans[i].setAttribute("data-note", note);
      }
      noteholder.innerHTML +=
        "<div class='footnote' id='_footnote_" + n + "'>" +
        "<a href='#_footnoteref_" + n + "' title='Return to text'>" +
        n + "</a>. " + note + "</div>";
      var id =spans[i].getAttribute("id");
      if (id != null) refs["#"+id] = n;
    }
  }
  if (n == 0)
    noteholder.parentNode.removeChild(noteholder);
  else {
    // Process footnoterefs.
    for (i=0; i<spans.length; i++) {
      if (spans[i].className == "footnoteref") {
        var href = spans[i].getElementsByTagName("a")[0].getAttribute("href");
        href = href.match(/#.*/)[0];  // Because IE return full URL.
        n = refs[href];
        spans[i].innerHTML =
          "[<a href='#_footnote_" + n +
          "' title='View footnote' class='footnote'>" + n + "</a>]";
      }
    }
  }
},

install: function(toclevels) {
  var timerId;

  function reinstall() {
    asciidoc.footnotes();
    if (toclevels) {
      asciidoc.toc(toclevels);
    }
  }

  function reinstallAndRemoveTimer() {
    clearInterval(timerId);
    reinstall();
  }

  timerId = setInterval(reinstall, 500);
  if (document.addEventListener)
    document.addEventListener("DOMContentLoaded", reinstallAndRemoveTimer, false);
  else
    window.onload = reinstallAndRemoveTimer;
}

}
// Generated by CoffeeScript 1.11.0

asciidoc.install(2);
/*]]>*/
</script>
<script type="text/javascript" src="./sequence-13_files/clipboard.min.js"></script><script type="text/javascript" src="./sequence-13_files/common.js"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 5px 0px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 5px; -webkit-border-radius: 5px; -moz-border-radius: 5px; -khtml-border-radius: 5px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 1px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: .7em}
.MathJax_MenuRadioCheck.RTL {right: .7em; left: auto}
.MathJax_MenuLabel {padding: 1px 2em 3px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #DDDDDD; margin: 4px 3px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: #606872; color: white}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
</style></head>
<body class="article"><div id="MathJax_Message" style="display: none;"></div>
<div id="header">
<h1>CA177 — Lab Sheet 5</h1>
<span id="author">Stephen Blott</span><br>
<span id="email"><code>&lt;<a href="mailto:stephen.blott@dcu.ie">stephen.blott@dcu.ie</a>&gt;</code></span><br>
<div id="toc">
  <div id="toctitle">Table of Contents</div>
  <noscript>&lt;p&gt;&lt;b&gt;JavaScript must be enabled in your browser to display the table of contents.&lt;/b&gt;&lt;/p&gt;</noscript>
<div class="toclevel1"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_tasks">1. Sequence Tasks</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_1">1.1. Sequence 1</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_2">1.2. Sequence 2</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_3">1.3. Sequence 3</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_4">1.4. Sequence 4</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_5">1.5. Sequence 5</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_6">1.6. Sequence 6</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_7">1.7. Sequence 7</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_8">1.8. Sequence 8</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_9">1.9. Sequence 9</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_10">1.10. Sequence 10</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_11">1.11. Sequence 11</a></div><div class="toclevel1"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_more_sequences">2. More Sequences</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_12">2.1. Sequence 12</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_13">2.2. Sequence 13</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_14">2.3. Sequence 14</a></div><div class="toclevel1"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequences_with_input">3. Sequences with Input</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_15">3.1. Sequence 15</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_16">3.2. Sequence 16</a></div><div class="toclevel2"><a href="https://ca177.computing.dcu.ie/labsheet-05-while-sequences.html#_sequence_17">3.3. Sequence 17</a></div></div>
</div>
<div id="content">
<div id="preamble">
<div class="sectionbody">
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Today, we start doing exercises involving <code>while</code> loops.  The notes are <a href="https://ca177.computing.dcu.ie/06-while-1.html">here</a>.</p></div>
</div></div>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>For all of the following tasks, you can upload and verify your solution on <em>Einstein</em>, <a href="https://ca177.computing.dcu.ie/einstein/">here</a>.</p></div>
</div></div>
</div>
</div>
<div class="sect1">
<h2 id="_sequence_tasks">1. Sequence Tasks</h2>
<div class="sectionbody">
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>In each of the following tasks, you will be presented with a sequence.
Your task is to output the first <strong>ten</strong> elements of the sequence to standard
output, one per line.</p></div>
<div class="paragraph"><p>Your solutions <strong>must</strong>
make good use of a <code>while</code> loop and
involve <em>at most one</em> print statement.</p></div>
</div></div>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Since you are always to output the first ten elements of a sequence, you
<em>know</em> how many times your loop should iterate.  Therefore, in these tasks
you should <em>always</em> use our pattern for <em>doing something N times</em>:</p></div>
<div class="listingblock">
<div class="content"><!-- Generator: GNU source-highlight 3.1.7
by Lorenzo Bettini
http://www.lorenzobettini.it
http://www.gnu.org/software/src-highlite -->
<pre class="clickCopyable" data-clipboard-text="i = 0
while i &lt; N:
   # Do something.
   i = i + 1" style="cursor: copy;"><tt>i <span style="color: #990000">=</span> <span style="color: #993399">0</span>
<span style="color: #0000FF">while</span> i <span style="color: #990000">&lt;</span> N<span style="color: #990000">:</span>
   <span style="font-style: italic"><span style="color: #9A1900"># Do something.</span></span>
   i <span style="color: #990000">=</span> i <span style="color: #990000">+</span> <span style="color: #993399">1</span></tt></pre></div></div>
<div class="paragraph"><p>The loop variable <code>i</code> takes on, in turn, each of the values from <code>0</code> to <code>N-1</code>, inclusive.</p></div>
</div></div>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>For each task you are given the first few elements of the sequence and the name of the Python script file to use.</p></div>
<div class="paragraph"><p>Your own output should be <em>one element per line</em>.</p></div>
</div></div>
<div class="sect2">
<h3 id="_sequence_1">1.1. Sequence 1</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-1.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-1.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 1 2 3 4 5 6 7 8 9</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_2">1.2. Sequence 2</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-2.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-2.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>1 2 3 4 5 6 7 8 9 10</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_3">1.3. Sequence 3</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-3.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-3.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 -1 -2 -3 -4 -5 -6 -7 -8 -9</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_4">1.4. Sequence 4</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-4.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-4.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 2 4 6 8 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_5">1.5. Sequence 5</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-5.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-5.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 3 6 9 12 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_6">1.6. Sequence 6</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-6.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-6.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 1 2 0 1 2 0 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_7">1.7. Sequence 7</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-7.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-7.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 2 4 0 2 4 0 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_8">1.8. Sequence 8</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-8.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-8.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 1 0 1 0 1 0 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_9">1.9. Sequence 9</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-9.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-9.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>1 0 1 0 1 0 1 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_10">1.10. Sequence 10</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-10.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-10.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>100 99 98 97 96 …</code></p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_11">1.11. Sequence 11</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-11.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-11.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 101 202 303 404 …</code></p></div>
</div></div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="_more_sequences">2. More Sequences</h2>
<div class="sectionbody">
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>The following tasks require similar loops to the previous tasks, but
additionally require you to maintain an extra state variable.</p></div>
</div></div>
<div class="sect2">
<h3 id="_sequence_12">2.1. Sequence 12</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-12.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-12.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 1 0 1 0 1 0 …</code></p></div>
<div class="paragraph"><p>Your solution <strong>must not</strong> involve the modulus operator (<code>%</code>).</p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_13">2.2. Sequence 13</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-13.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-13.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 1 3 6 10 15 …</code></p></div>
<div class="paragraph"><p>Explanation:</p></div>
<div class="ulist"><ul>
<li>
<p>
<code>0</code> is <code>0</code>
</p>
</li>
<li>
<p>
<code>1</code> is <code>0 + 1</code>
</p>
</li>
<li>
<p>
<code>3</code> is <code>0 + 1 + 2</code>
</p>
</li>
<li>
<p>
<code>6</code> is <code>0 + 1 + 2 + 3</code>
</p>
</li>
<li>
<p>
<code>10</code> is <code>0 + 1 + 2 + 3 + 4</code>
</p>
</li>
<li>
<p>
and so on.
</p>
</li>
</ul></div>
<div class="paragraph"><p>In other words, you must keep track of the sum of the values of <code>i</code> encountered so far.</p></div>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_14">2.3. Sequence 14</h3>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Script name: <code class="clickCopyable" data-clipboard-text="sequence-14.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-14.py</code></p></div>
<div class="paragraph"><p>Sequence: <code>0 2 0 2 0 2 0 …</code></p></div>
<div class="paragraph"><p>Your solution <strong>must not</strong> involve the modulus operator (<code>%</code>).</p></div>
</div></div>
</div>
</div>
</div>
<div class="sect1">
<h2 id="_sequences_with_input">3. Sequences with Input</h2>
<div class="sectionbody">
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>Above, your solutions are all required to produce exactly ten terms of the required sequence.</p></div>
<div class="paragraph"><p>Below, you must read the number of terms required from standard input.</p></div>
</div></div>
<div class="sidebarblock">
<div class="content">
<div class="paragraph"><p>A good solution does not use the exponent operator, <code>**</code>.</p></div>
</div></div>
<div class="sect2">
<h3 id="_sequence_15">3.1. Sequence 15</h3>
<div class="sidebarblock">
<div class="content">
<div class="title">Task</div>
<div class="paragraph"><p>Write a Python script named <code class="clickCopyable" data-clipboard-text="sequence-15.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-15.py</code> which reads a positive integer
<code>n</code> from standard input and outputs the first <code>n</code> terms of the sequence:</p></div>
<div class="ulist"><ul>
<li>
<p>
<code>1 2 4 8 16 32 …</code>
</p>
</li>
</ul></div>
</div></div>
<div class="listingblock">
<div class="title">Example standard input</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="5" style="cursor: copy;"><code>5</code></pre>
</div></div>
<div class="listingblock">
<div class="title">Example standard output</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="1
2
4
8
16" style="cursor: copy;"><code>1
2
4
8
16</code></pre>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_16">3.2. Sequence 16</h3>
<div class="sidebarblock">
<div class="content">
<div class="title">Task</div>
<div class="paragraph"><p>Write a Python script named <code class="clickCopyable" data-clipboard-text="sequence-16.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-16.py</code> which reads a positive integer
<code>n</code> from standard input and outputs the first <code>n</code> terms of the sequence:</p></div>
<div class="ulist"><ul>
<li>
<p>
<code>n-1 n-2 n-3 … 0</code>
</p>
</li>
</ul></div>
</div></div>
<div class="listingblock">
<div class="title">Example standard input</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="5" style="cursor: copy;"><code>5</code></pre>
</div></div>
<div class="listingblock">
<div class="title">Example standard output</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="4
3
2
1
0" style="cursor: copy;"><code>4
3
2
1
0</code></pre>
</div></div>
</div>
<div class="sect2">
<h3 id="_sequence_17">3.3. Sequence 17</h3>
<div class="sidebarblock">
<div class="content">
<div class="title">Background</div>
<div class="paragraph"><p>The Hailstone sequence is the sequence of positive integers generated by
repeatedly applying the following rule:</p></div>
<div class="ulist"><ul>
<li>
<p>
if the current term is even, then generate the next term by dividing the current term by two,
</p>
</li>
<li>
<p>
otherwise, generate the next term by multiplying the current term by three and adding one.
</p>
</li>
</ul></div>
<div class="paragraph"><p>Here’s an example beginning with <code>11</code>.</p></div>
<div class="listingblock">
<div class="content">
<pre class="clickCopyable" data-clipboard-text="11 34 17 52 26 13 40 20 10 5 16 8 4 2 1" style="cursor: copy;"><code>11 34 17 52 26 13 40 20 10 5 16 8 4 2 1</code></pre>
</div></div>
<div class="paragraph"><p>Curiously, it is thought (but not proven) that, no matter what initial term
is chosen, the sequence eventually reaches <code>1</code>.</p></div>
</div></div>
<div class="sidebarblock">
<div class="content">
<div class="title">Task</div>
<div class="paragraph"><p>Write a Python script named <code class="clickCopyable" data-clipboard-text="sequence-17.py" title="You have not yet attempted this task." style="cursor: copy;">sequence-17.py</code> which reads <em>two</em> positive integers
from standard input, <code>v</code> a value and <code>n</code> a number, and outputs the next <code>n</code> terms of the hailstone sequence starting at <code>v</code>.</p></div>
</div></div>
<div class="listingblock">
<div class="title">Example standard input</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="11
5" style="cursor: copy;"><code>11
5</code></pre>
</div></div>
<div class="listingblock">
<div class="title">Example standard output</div>
<div class="content">
<pre class="clickCopyable" data-clipboard-text="11
34
17
52
26" style="cursor: copy;"><code>11
34
17
52
26</code></pre>
</div></div>
<script src="./sequence-13_files/instrument.js"></script>
<script type="text/javascript" src="./sequence-13_files/MathJax.js">
</script>
</div>
</div>
</div>
</div>

<div id="footer">
<div id="footer-text">
Last updated
 2017-02-27 08:44:28 GMT
</div>
</div>


<p id="pointerText" style="z-index: 1000000000; position: absolute; background: rgb(243, 243, 243); border: 2px solid rgb(222, 222, 222); padding: 3px; border-radius: 4px; white-space: nowrap; font-size: 11px; left: 328px; top: 2720px; display: none;">Text copied to the clipboard.</p><textarea readonly="" style="font-size: 12pt; border: 0px; padding: 0px; margin: 0px; position: absolute; left: -9999px; top: 2568px;"></textarea></body></html>