from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

styles = r'''

/* Geometrically centered cover arrow drawn with CSS. */
.open-btn .arrow{
    position:absolute;
    left:50%;
    top:50%;
    width:52px;
    height:22px;
    margin:0;
    font-size:0;
    line-height:0;
    transform:translate(-50%,-50%);
    animation:none!important;
}
.open-btn .arrow::before{
    content:"";
    position:absolute;
    left:0;
    top:50%;
    width:42px;
    height:2px;
    background:#fff8ef;
    border-radius:2px;
    transform:translateY(-50%);
}
.open-btn .arrow::after{
    content:"";
    position:absolute;
    right:0;
    top:50%;
    width:12px;
    height:12px;
    border-top:2px solid #fff8ef;
    border-right:2px solid #fff8ef;
    transform:translateY(-50%) rotate(45deg);
    transform-origin:center;
}
'''

if '/* Geometrically centered cover arrow drawn with CSS. */' not in text:
    text = text.replace('</style>', styles + '\n</style>', 1)

path.write_text(text, encoding='utf-8')
