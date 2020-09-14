/* -22px = (f(x) =  3)
    24px = (f(x) =  0)
    70px = (f(x) = -3)
    */
//Here I made some of the Math functions more user friendly
var sin = Math.sin;
var cos = Math.cos;
var tan = Math.tan;
var pi = Math.pi;
// This is what gets called by the button
function compute(fnct) {
  var fnct = document.getElementById('fnct').value; //getting the value from the input
  var points = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']
  /* The individual points get cycled through with this array,
  and then their y-value is changed individually */
  for (var i = -3, j = 0; i <= 3.1;i += .6, j++) {
  var newFnct = eval(fnct.replace(/x/g, ('('+Math.round(i*100)/100)+')') ); //the extra parentheses make it possible to understand exponentials
    
  var texty = document.getElementById(points[j]).style.top = Math.round(newFnct*(46/(-3))+24)+'px';
  }
}
document.querySelector("#fnct").addEventListener("keyup", event => {
    if(event.key !== "Enter") return; // Use `.key` instead.
    document.querySelector("#cmpButton").click(); // Things you want to do.
    event.preventDefault(); // No need to `return false;`.
});
