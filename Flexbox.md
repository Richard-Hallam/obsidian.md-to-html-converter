Flexbox is  a css tool to arrange content within a container. You set a container to be a flexbox by using `display:flex` 

Flexboxes have multiple properties to arrange content they are as follows.

<h3>flex-direction</h3>
The flex direction property defines in which direction the container wants to stack the flex items. It it configured by passing it the following values.

	`flex-direction: column` 
This stacks the flex items vertically from top to bottom

	`flex-direction: reverse-column`
This stacks the flex items vertically in reverse order.

	`flex-direction: row`
This stacks the flex items horizontally from left to right.
	`flex-direction: row-reverse`
This stacks the flex items horizontally from right to left.

when you set the direction to a reversed row or column, start and end are also reversed.

Notice that when the flex direction is a column, `justify-content` changes to the vertical and `align-items` to the horizontal.
<h3>flex-wrap</h3>
The `flex-wrap` property specifies whether the flex items should wrap or not. Wrapping prevents flex items being forced onto a single line.

if given the value `nowrap` then flex items are forced onto a single line.

if given the value `wrap` then the items will flow onto multiple lines if needed.

`wrap-reverse` will wrap onto multiple lines but reverse the order.

<h3>flex-flow</h3>
The `flex-flow` property is a shorthand for setting both the `flex-direction` and `flex-wrap` properties.

its usage is `flex-flow: row wrap;`

<h3>justify-content</h3>
The `justify-content` property is used to align the flex items.

values are as follows
	`center`
	`flex-start`
	`flex-end`
	`space-around`--displays the flex items with space before, between and after the lines
	`space-between`--displays the flex items with space between the lines.

<h3>align-items</h3>
The `align-items` property is used to align the flex items within the container.

values are as follows
	`center`--middle of the container
	`flex-start`--top of the container
	`flex-end`--bottom of the container
	`stretch`--Stretches the flex items to fill the container. This is the default value.
	`baseline`--aligns to the baseline for example the text baseline.


<h3>align-content</h3>
The `align-content` property is used to align the lines of flex items

values are as follows
	`space-between`--displays the flex lines with equal space between them.
	`space-around`--displays the flex lines with space before, between and after them
	`center`--middle of the container
	`flex-start`--top of the container
	`flex-end`--bottom of the container
	`stretch`--Stretches the flex items to fill the container. This is the default value.


<h3>Summary</h3>

| **property**          | **What does it do?**                                                                                                                                                                          | **Default value** | **Other values**                                                            |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------------------------------------------------------- |
| flex-direction        | This controls how the child elements are arranged by setting the **main axis** (horizontal for row, vertical for column) and direction (left to right or reversed, top to bottom or reversed) | row               | column  <br>row-reverse  <br>column-reverse                                 |
| flex-wrap             | Controls whether elements are allowed to wrap to a new row/column if there isn’t enough space                                                                                                 | nowrap            | wrap  <br>wrap-reverse                                                      |
| justify-content       | Controls how elements are distributed along the **main axis** (described above)                                                                                                               | flex-start        | flex-end  <br>center  <br>space-between  <br>space-around  <br>space-evenly |
| align-items           | Controls how elements are distributed on the **cross axis** (opposite to the **main axis** , as described above)                                                                              | stretch           | flex-start  <br>flex-end  <br>center  <br>baseline                          |
| gap                   | Sets a **minimum** space **between** elements.                                                                                                                                                | 0px               | length (e.g. 10px)                                                          |
| Flex-flow (shorthand) | Sets flex-direction and flex-wrap in a single property                                                                                                                                        | row nowrap        | See **flex-direction** and **flex-wrap**                                    |
