(function (lib, img, cjs, ss) {

var p; // shortcut to reference prototypes

// library properties:
lib.properties = {
	width: 728,
	height: 90,
	fps: 23,
	color: "#FFFFFF",
	manifest: [
		{src:"images/img_1.jpg", id:"img_1"},
		{src:"images/whoosh.jpg", id:"whoosh"}
	]
};



// symbols:



(lib.img_1 = function() {
	this.initialize(img.img_1);
}).prototype = p = new cjs.Bitmap();
p.nominalBounds = new cjs.Rectangle(0,0,728,90);


(lib.whoosh = function() {
	this.initialize(img.whoosh);
}).prototype = p = new cjs.Bitmap();
p.nominalBounds = new cjs.Rectangle(0,0,384,90);


(lib.whsh = function() {
	this.initialize();

	// Layer 1
	this.instance = new lib.whoosh();

	this.addChild(this.instance);
}).prototype = p = new cjs.Container();
p.nominalBounds = new cjs.Rectangle(0,0,384,90);


(lib.white = function() {
	this.initialize();

	// Layer 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("Eg43AHCIAAuDMBxvAAAIAAODg");
	this.shape.setTransform(364,45);

	this.addChild(this.shape);
}).prototype = p = new cjs.Container();
p.nominalBounds = new cjs.Rectangle(0,0,728,90);


(lib.Symbol8 = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Layer 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(32,171,229,0.898)").s().p("A3bTiMAAAgnDMAu2AAAMAAAAnDg");
	this.shape.setTransform(150,125);
	this.shape._off = true;

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(3).to({_off:false},0).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = null;


(lib.Symbol1 = function() {
	this.initialize();

	// Layer 3
	this.instance = new lib.img_1();
	this.instance.setTransform(0,0.5);

	this.addChild(this.instance);
}).prototype = p = new cjs.Container();
p.nominalBounds = new cjs.Rectangle(0,0,728.1,90.5);


(lib.whsh_Mc = function() {
	this.initialize();

	// Layer 3
	this.shape = new cjs.Shape();
	this.shape.graphics.lf(["rgba(6,159,222,0)","#069FDE","#069FDE","rgba(6,159,222,0)"],[0,0.545,0.718,1],-602.5,0,602.5,0).s().p("EheHAHCIAAuDMC8PAAAIAAODg");
	this.shape.setTransform(-886.5,45);

	// Layer 1 copy
	this.instance = new lib.whsh();
	this.instance.setTransform(-574,45,1,1,0,0,180,192,45);

	// Layer 1
	this.instance_1 = new lib.whsh();
	this.instance_1.setTransform(-192,45,1,1,0,0,0,192,45);

	// Layer 2 copy
	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("Eg5oAHCIAAuDMBzRAAAIAAODg");
	this.shape_1.setTransform(360,45);

	this.addChild(this.shape_1,this.instance_1,this.instance,this.shape);
}).prototype = p = new cjs.Container();
p.nominalBounds = new cjs.Rectangle(-1489,0,2218,90);


// stage content:
(lib.N475_A2_728x90 = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// timeline functions:
	this.frame_0 = function() {
		root = this;
		this.addEventListener("click", clickThru);
		function clickThru(){
			//window.open(clickTag, "_blank");
			//EB.clickthrough();
			Enabler.exit('htmlExit1');
		}
	}
	this.frame_216 = function() {
		this.stop();
	}

	// actions tween:
	this.timeline.addTween(cjs.Tween.get(this).call(this.frame_0).wait(216).call(this.frame_216).wait(25));

	// ClikTag
	this.instance = new lib.Symbol8();
	this.instance.setTransform(364,45,2.427,0.36,0,0,0,150,125);
	new cjs.ButtonHelper(this.instance, 0, 1, 2, false, new lib.Symbol8(), 3);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(241));

	// border
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#CCCCCC").ss(1,1,1).p("Eg4ygG8MBxlAAAIAAN5MhxlAAAg");
	this.shape.setTransform(364,45);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(241));

	// white
	this.instance_1 = new lib.white();
	this.instance_1.setTransform(364,45,1,1,0,0,0,364,45);
	this.instance_1.alpha = 0;
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(217).to({_off:false},0).to({alpha:1},12).wait(12));

	// whoosh
	this.instance_2 = new lib.whsh_Mc();
	this.instance_2.setTransform(192,45,1,1,0,0,0,192,45);

	this.timeline.addTween(cjs.Tween.get(this.instance_2).to({x:2422},46).to({_off:true},1).wait(194));

	// img
	this.instance_3 = new lib.Symbol1();
	this.instance_3.setTransform(364,45,1,1,0,0,0,364,45);

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(241));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-1125,44.5,2218,91);

})(lib = lib||{}, images = images||{}, createjs = createjs||{}, ss = ss||{});
var lib, images, createjs, ss;