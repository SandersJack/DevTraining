#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;


void main() {
    vec2 uv = (gl_FragCoord.xy )/ u_resolution.xy;

	float t = u_time;
	

    vec2 pos = fract(uv*1.) - 0.5;

	
	float eq_x = 10.*pow(pos.x,2.) + 0.5*pos.x + 7.; 
	float eq_y = 10.*pow(pos.y,2.) + 0.5*pos.y + 7.; 

	float r = 10./exp(t*eq_x/10.*1.25+2.0);
	bool check = false;
	if (r < 0.01){
		//r = 0.2;
		check = true;
	} 
	if (check) {
		r = 10./cos(t*eq_y*pow(eq_x,2.)/10.*1.25+2.0);
		check = false;
	}
	//float circles = (sqrt(abs(cir.x+cir.y*0.5)*25.0)*5.0);
	gl_FragColor = vec4(pow(r,1.),0.1/abs(sin(eq_y*t/2.-1.0)-sin(eq_x)),0.1/abs(sin(t/10.*eq_y*eq_x)*1.0),1.);
}	