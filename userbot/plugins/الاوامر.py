# WRITE  BY @VUUZZ - @RR9R7
# PLUGIN FOR JepThon USERBOT
# @JepThon

import random
from telethon import events
import random, re

from userbot.utils import admin_cmd

import asyncio
from userbot import jmthon

from ..core.managers import edit_or_reply

plugin_category = "extra"

@jmthon.ar_cmd(
    pattern="الاوامر$",
    command=("الاوامر", plugin_category),
)
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
        "** 𓆩قہائمہة اوامہر سہورس جہيہبہثہون𓆪 **  :\n 𓍹——————❁ＪΞＰ❁——————𓍻\n( `.م1` )  - اوامر الادمن\n( `.م2` )  - اوامر المجموعة\n( `.م3` )  -  اوامر الترحيب والردود\n( `.م4` )  - حماية خاص والتلكراف\n( `.م5` )  - اوامر المنشن والانتحال\n( `.م6` )  - اوامر التحميل والترجمة\n( `.م7` )  - اوامر المنع و القفل\n( `.م8` )  - اوامر التنظيف والتكرار\n( `.م9` )  - اوامر التخصيص والفارات\n( `.م10` )  - اوامر الوقتي و التشغيل\n( `.م11` )  - اوامر الكشف و الروابط\n( `.م12` )  - اوامر المساعدة والإذاعة \n( `.م13` )  - اوامر الارسال والاستغفار\n( `.م14` )  - اوامر المـلصقات وكوكل\n( `.م15` ) - اوامر التسلية والتحشيش \n( `.م16` ) - اوامر الصيغ والجهات\n( `.م17` ) - اوامر التمبلر والزغرفة والمتحركة\n( `.م18` ) - اوامر الحساب والالعاب\n𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙[ ┈┉━｢ ＪΞＰＴΗＯＮ ｣━┅┈ ](t.me/jepthon)"
)

@jmthon.ar_cmd(
    pattern="م1$",
    command=("م1", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الادمن لسورس جـيبثون **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)
		
@jmthon.ar_cmd(
    pattern="م2$",
    command=("م2", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المجـموعه لسورس جـيبثون **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م3$",
    command=("م3", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـترحيب والـردود **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الترحيب` )\n- ( `.اوامر الردود` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="م4$",
    command=("م4", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر حـماية الخاص والتلكراف **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الخاص` )\n- ( `.اوامر التلكراف` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="م5$",
    command=("م5", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الـمنشن والانتحال **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الانتحال` )\n- ( `.اوامر التقليد` )\n- ( `.اوامر المنشن` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م6$",
    command=("م6", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التحميل والترجمه **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر النطق` )\n- ( `.اوامر التحميل` )\n- ( `.اوامر الترجمة` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م7$",
    command=("م7", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر القفل والمنع **:\n𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر القفل` )\n- ( `.اوامر الفتح` )\n- ( `.اوامر المنع` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م8$",
    command=("م8", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التكرار والتنظيف **:\n𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التكرار` )\n- ( `.اوامر السبام` )\n- ( `.اوامر التنظيف` ) \n- ( `.اوامر المسح` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م9$",
    command=("م9", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الفارات والتخصيص **:\n هـنـا  : \n\n@Jepthon2"
		)

@jmthon.ar_cmd(
    pattern="م10$",
    command=("م10", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الوقتي والتشغيل **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الاسم` )\n- ( `.اوامر البايو` )\n- ( `.اوامر التشغيل` ) \n- ( `.اوامر الاطفاء` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)	

@jmthon.ar_cmd(
    pattern="م11$",
    command=("م11", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الكـشف و الروابط **:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الكشف` )\n- ( `.اوامر الروابط` ) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="م12$",
    command=("م12", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر المساعدة  **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الوقت والتاريخ` )\n- ( `.اوامر كورونا` )\n- ( `.اوامر الصلاة` ) \n- ( `.اوامر مساعدة` )\n- ( `.اوامر الاذاعه` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="م13$",
    command=("م13", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الارسال **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.امر الصورة الذاتية` )\n- ( `.اوامر التحذيرات` )\n- ( `.اوامر اللستة` )\n- ( `.اوامر الملكية` ) \n- ( `.اوامر السليب` ) \n- ( `.اوامر الاستغفار` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)
@jmthon.ar_cmd(
    pattern="م14$",
    command=("م14", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الملصقات وكوكل **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الملصقات` )\n- ( `.اوامر كوكل` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م15$",
    command=("م15", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر التسلية والتحشيش **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التسلية` )\n- ( `.اوامر التحشيش` )\n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م16$",
    command=("م16", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر تحويل الصيغ و الجهات **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر التحويل` )\n- ( `.اوامر الجهات` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"
)

@jmthon.ar_cmd(
    pattern="م18$",
    command=("م18", plugin_category),
)
async def _(event):
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit(
		"** قائمة اوامر الحساب و الالعاب **:\n 𓍹——————❁ＪΞＰ❁——————𓍻\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اوامر الحساب` )\n- ( `.اوامر الالعاب` ) \n𓍹——————❁ＪΞＰ❁——————𓍻\n⌔︙CH : @JepThon"

)
