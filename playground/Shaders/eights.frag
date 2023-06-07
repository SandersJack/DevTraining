#ifdef GL_ES
precision mediump float;
#endif 

uniform vec2 u_resolution;
uniform float u_time;


void main() {
    vec2 uv = (gl_FragCoord.xy )/ u_resolution.xy;


    vec2 pos = (uv.xy-0.5);
	vec2 cir = ((pos.xy*pos.xy+sin(uv.x*18.0+u_time)/25.0*sin(uv.y*7.0+u_time*1.5)/1.0)+uv.x*sin(u_time)/16.0+uv.y*sin(u_time*1.2)/16.0);
	float circles = (sqrt(abs(cir.x+cir.y*0.5)*25.0)*5.0);
	gl_FragColor = vec4(sin(circles*1.25+2.0),abs(sin(circles*1.0-1.0)-sin(circles)),abs(sin(circles)*1.0),1.0);
}