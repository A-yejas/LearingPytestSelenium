'''
Action Chains:--
->>>click(on_element: WebElement | None = None) → ActionChains
Clicks an element.
Args:
on_element: The element to click. If None, clicks on current mouse position.
->>>click_and_hold(on_element: WebElement | None = None) → ActionChains
Holds down the left mouse button on an element.
Args:
on_element: The element to mouse down. If None, clicks on current mouse position.
->>>context_click(on_element: WebElement | None = None) → ActionChains
Performs a context-click (right click) on an element.
Args:
on_element: The element to context-click. If None, clicks on current mouse position.
->>>double_click(on_element: WebElement | None = None) → ActionChains
Double-clicks an element.
Args:
on_element: The element to double-click. If None, clicks on current mouse position.

->>>drag_and_drop(source: WebElement, target: WebElement) → ActionChains
Holds down the left mouse button on the source element, then moves to the target element and releases the mouse button.

Args:
source: The element to mouse down.

target: The element to mouse up.

->>>drag_and_drop_by_offset(source: WebElement, xoffset: int, yoffset: int) → ActionChains
Holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button.

Args:
source: The element to mouse down.

xoffset: X offset to move to.

yoffset: Y offset to move to.

->>>key_down(value: str, element: WebElement | None = None) → ActionChains
Sends a key press only, without releasing it. Should only be used with modifier keys (Control, Alt and Shift).

Args:
value: The modifier key to send. Values are defined in Keys class.

element: The element to send keys. If None, sends a key to current focused element.

Example, pressing ctrl+c:
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
->>>key_up(value: str, element: WebElement | None = None) → ActionChains
Releases a modifier key.
Args:
value: The modifier key to send. Values are defined in Keys class.

element: The element to send keys. If None, sends a key to current focused element.

Example, pressing ctrl+c:
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
->>>move_by_offset(xoffset: int, yoffset: int) → ActionChains
Moving the mouse to an offset from current mouse position.

Args:
xoffset: X offset to move to, as a positive or negative integer.

yoffset: Y offset to move to, as a positive or negative integer.

->>>move_to_element(to_element: WebElement) → ActionChains
Moving the mouse to the middle of an element.

Args:
to_element: The WebElement to move to.

->>>move_to_element_with_offset(to_element: WebElement, xoffset: int, yoffset: int) → ActionChains
Move the mouse by an offset of the specified element. Offsets are relative to the in-view center point of the element.

Args:
to_element: The WebElement to move to.

xoffset: X offset to move to, as a positive or negative integer.

yoffset: Y offset to move to, as a positive or negative integer.

->>>pause(seconds: float | int) → ActionChains
Pause all inputs for the specified duration in seconds.

->>>perform() → None
Performs all stored actions.

->>>release(on_element: WebElement | None = None) → ActionChains
Releasing a held mouse button on an element.

Args:
on_element: The element to mouse up. If None, releases on current mouse position.

->>>reset_actions() → None
Clears actions that are already stored locally and on the remote end.

->>>scroll_by_amount(delta_x: int, delta_y: int) → ActionChains
Scrolls by provided amounts with the origin in the top left corner of the viewport.

Args:
delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.

delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.

->>>scroll_from_origin(scroll_origin: ScrollOrigin, delta_x: int, delta_y: int) → ActionChains
Scrolls by provided amount based on a provided origin. The scroll origin is either the center of an element or the upper left of the viewport plus any offsets. If the origin is an element, and the element is not in the viewport, the bottom of the element will first be scrolled to the bottom of the viewport.
Args:
origin: Where scroll originates (viewport or element center) plus provided offsets.
delta_x: Distance along X axis to scroll using the wheel. A negative value scrolls left.
delta_y: Distance along Y axis to scroll using the wheel. A negative value scrolls up.
Raises:
If the origin with offset is outside the viewport. - MoveTargetOutOfBoundsException - If the origin with offset is outside the viewport.
-------------
->>>scroll_to_element(element: WebElement) → ActionChains
If the element is outside the viewport, scrolls the bottom of the element to the bottom of the viewport.
Args:
element: Which element to scroll into the viewport.
---------
->>>send_keys(*keys_to_send: str) → ActionChains
Sends keys to current focused element.
Args:
keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.
-------------
->>>send_keys_to_element(element: WebElement, *keys_to_send: str) → ActionChains
Sends keys to an element.
Args:
element: The element to send keys.
keys_to_send: The keys to send. Modifier keys constants can be found in the ‘Keys’ class.
'''
