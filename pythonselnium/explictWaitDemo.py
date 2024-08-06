'''
Q:-Welcome back.
let's see how to use explicit wait

So problem here is with implicit weight you are actually waiting.
Wherever the element is not displayed, you are waiting for 5 seconds and if it displays before that,
you are continuing.
Right, which is good.

I agree.

Now let's say this guy promo code.

So now it will keep on running, right?

So let's say it might take 10 seconds.

So all your application maximum will take 5 seconds to load.

But this is a special case in your application where it may take up to 10 seconds or 15 seconds.

Okay, so then what will you do?

So if somebody tells you that, hey, this will take you 15 seconds, then if you are on implicit weight,

you will say, okay, let me update to 15, fine.

But there is one disadvantage here.

Now, let's say if this element is not real, really appearing there is a bug.

So when will our selenium test fail?

It will fail only after 15 seconds, right?

Because until 15 seconds it will keep on waiting for it.

But technically your entire application is maximum wait for only 5 seconds.

If it does not load in 5 seconds, I'm sure that your application have issue.

That is how you know about your application.

There is only one case where it will take 15 seconds because maybe let's take an example of a table.

Table, have some 10,000 records to fetch, right?

So it might take 15 seconds just because one scenario is demanding 15 seconds, you are unnecessarily

applying that 15 seconds globally to each and every line of your script.

That's a bad right.

So there is no harm in waiting.

But problem is, if it does not display in 5 seconds, you know there is a bug.

Even after knowing that there is a bug in 52nd, you are wasting another 10 seconds every time, right?

15 seconds.

It will not tell if it's an issue.

So that's not good case.

So if you put back to 5 seconds because your application is mostly on file, this case will fail because

this is demanding 15.

So here where explicit weight comes into picture.

So in explicit weight, you can actually target one specific element and you can set exclusively or

explicitly to that particular element up to 15 seconds.

So when you do that, it overrides the implicit weight and applies explicit weight for that particular

step.

That is what we need, right?

So let it be 5 seconds globally.

But if you know that this particular case where after you click that the text will take around 15 seconds

here, where for this particular element you can target of writing explicit weight.

That's my thought process here.

That is how people will do in real time to target that.

Okay.

So how do you declare explicit weight?

It's again, very simple, guys.

So you just need to create one object of the class card, web driver weight.

So there is one class defined.

If you hover your cursor, then it will ask you to import that package.

So here, this class expects two arguments.

One is you are a driver object of your whole web driver and how many seconds you want to wait.

Let's say this displays in 10 seconds because 5 seconds is globally applied, but one particular element

is demanding 10 seconds.

So you put into one object.

So weight is an object which no information about how much time it has to wait and everything.

Now on this weight object there is a method called until so very dot until so up to how much time you

want to wait.

You want to wait until this promo info text displayed, right?

So now let's see.

I'll reply, I'll remove all this and I'll bring that to initial state.

Give me a second.

So right now there is no code applied text, right?

When I click on a play.

Okay.

That is empty court.

The whole city.

I'll read something like this.

And when I click and I play.

Let's see.

Invalid code, whatever it is.

So when you hover it promo info, this is the class, right?

This is the class which gets generated with some message.

So when you land on the screen for first time, do you see the class dot class name?

See that class is not there.

The text is not at all present.

When that text is showing, that text is showing only after the message shows up here.

When that message will show up, that will show up after 5 seconds or 10 seconds.

We don't know.

Right.

See, the message is still not showing up.

Zero elements, matching zero elements.

Let's wait.

And now we will see one element matching.

So once this text is displayed, then we know that this particular cursor selector is up here in the

page.

So now what we can do here smartly, we can say, wait until there is something called expected conditions.

Just follow me.

By end of this lecture, you will understand what I'm trying to do here.

Hover your cursor to import that package as well.

So Veidt does not presence of element located or visibility of element located.

A lot of things we are saying, wait until that element is located on the page.

Wait until that visibility of that element located on page or wait until that text is present on that

element.

Wait until title is there.

See, all these are things we have in our case.

Wait until that is visible on the screen.

Right.

Visibility or presence.

Presence is also matters because right now there is no presence.

When you refresh and there is no text here, do you see any presence?

Let's see.

I'll refresh it again.

There is no promo code.

Right.

It can enter.

No presence, is there.

You click on apply button and you will wait on presence displayed.

So we will say like this wait until the presence of element located with what says a selector, because

this method is expecting to have a find element criteria.

So find element criterion means by dot CSS selector and provide that says selector simple.

So now you interpret this code here.

First we created object based on web driver weight class.

So here we set a timeout to 10 seconds.

So this way to object know that it has to wait until 10 seconds.

Fine.

Now it's waiting.

But for what it is waiting.

That information you have to give in this until method.

Wait until when you give this expected condition.

What is your expected condition?

So I want to wait until this particular CSS selector is presence is located on the web page.

So what it does is it overrides implicit wait and it wait up to 10 seconds to see whether this particular

CSS is loaded on the page.

Let's say if it loaded in 3 seconds, that fine it resumes, it will not wait until ten, just like

implicit behavior whenever it finds it resumes.

But the beauty here is we are targeting only this 10 seconds to this CSS selector.

Once you come out of this, this is no more valid, right?

Because this wait, we are playing of 10 seconds greater timeout only for this.

Yes.

Selector to display on the page, not for any other step.

But if you declare implicit weight globally, that applies to every step, explicit way.

It is something where your target one element to show up by giving expected conditions and until method.

So what I suggest is better to have both implicit and explicit weight in your framework.

Implicit weight is simply globally applied.

The based timeout where your application might take to load pages explicit rate is something where exceptionally

some things take a lot of time to load, but if it takes some 100 seconds, don't update your implicit

weight because that's a global and it will have impact on your overall tests in the framework.

Instead, only target that particular element by writing like this, create a web driver weight class

object and say until do whatever condition you want, put it and give the information.

Right?

So it will wait until that is displayed and then it will happily get the text.

That's the magic.

So I'll still go with this.

5 seconds.

Wait, this is taking more than 5 seconds, but good.

Now we have explicit weight in place.

Let's see.

These are famous interview questions, guys.

The last two lectures, what I explain now, you may get a lot of questions that went to use explicit

when to use implicit difference between them.

Why can't I use time or sleep?

So all these are pretty important.

And the example what is shown is a classic one.

So all this taking one second to load for me, but this is something which is taking more than 5 seconds

or 2 seconds and.

Yeah.

Oh, it failed, guys.

Let's see.

Presence of elements.

Take one personal argument, but two were given.

Where did we give two?

I know why I think we missed this piece here.

There is one more practice needed.

And here also.

Third one is needed.

Good.

So basically this piece, whatever we are writing, that should be this is first bracket, right?

The first bracket ended here and the second bracket we open that ended here.

And the third one, which is your bite out element, should be written like this.

So brackets are missing.

That's why it would fail.

Let's run again.

This time it should pass.

But before running, I'll do one thing.

I'll put this implicit rate.

Only 2 seconds.

Because just to go another page, all that hardly 2 seconds is required only for this loading.

It is taking more than 2 seconds.

For that I will smartly use explicit weight OC.

But if I don't use explicit weight and then put only 2 seconds here, then your test will fail at that

code applied because code applied is taking more than 2 seconds.

Now we need not worry because there is explicit weight there.

So overall it is maximum 2 seconds, but at this pace it's taking the time, whatever.
Code applied and exit code zero.
That's how you differentiate explicit and implicit

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=(len(results))
assert count > 0
#chaining element
#You are chaining your parent web element to child web element to construct dynamically.This concept as chaining of web elements.

for result in results:
    result.find_element(By.XPATH, "div/button").click()



driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == total_amount



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
