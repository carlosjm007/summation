// http://p5js.org/reference/#/p5.Element/parent
var $N = 1;
var espacio;
var $cubo;
var oo;
var $trans = [];

function calculo(N){
	espacio = 400/N;
	$cubo = espacio/7;
	$trans = [];
	for(oo = 0 ; oo < N ; oo = oo + 1){
		$trans[oo] = espacio;
	}
}
function setup() {
	var u = createCanvas(500, 500, WEBGL);
	u.parent("cubo");
}

function draw() {
	background(255);
	orbitControl();
	rotateY(map(mouseX, 0, width, 0, PI));
	rotateX(map(mouseY, 0, height, 0, PI));
	translate(-200, -200, -200);
	var i, j, k;
	calculo($N);
	for(i in $trans){
		translate(0, 0, $trans[i]);
		for(j in $trans){
			translate(0, $trans[j], 0);
			for(k in $trans){
				box($cubo);
				translate($trans[k], 0, 0);
			}
			translate(-400, 0, 0);
		}
		translate(0, -400, 0);
	}
}