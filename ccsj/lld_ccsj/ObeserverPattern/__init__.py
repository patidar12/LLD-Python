'''

Obervable: entity which is obervable.

Obeserver: entity which oberver Obervable. And hit event when some udate happen in Obervable.

For Ex.:
We are using mobile and tv screen for whether temprature.
So here, whether temrature is Observable and mobile screen or Tv scrren is Observer that Hit some evnt when
There is a change in whether temrature(Observer).

One more example is Notify Me Button on Ecoomerce Sites or any other platfor.

Here, Let say whenever a item is out of stock we are providing, Notify me button.
And when theu se hit the Notify me button then we have to record that whenever that item is
In stock we have to Notify that user. We can notify that user in different way.
For ex. -> either on mobile or on Email.

So here. Stocks Of Items Is Observable. And EmailNotifier and MObilerNotifier is Obesrver.

So whenver any Item (ex: Iphone, Tv, Mixer) Is in stock we have to send events to all the User Using Type Of Observer (EmailNotifier or MobileNotifier).

'''