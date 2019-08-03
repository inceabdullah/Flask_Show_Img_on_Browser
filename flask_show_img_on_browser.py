import io
from flask import Flask, request, send_file
app = Flask(__name__)


import make_fittedFRAMED_textIMG

@app.route('/make-text-img', methods=['GET'])
def text_img():
    
    



	def serve_pil_image(pil_img):
		img_io = io.BytesIO()
		pil_img.save(img_io, 'PNG', quality=70)
		img_io.seek(0)
        
		return send_file(img_io, mimetype='image/jpeg')   
	img = make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG("BakÄ±n da ne dedi??", False, 24, "bg_320x50.png", True, (220,100),18)[0] 
        
	# img = Image.new('RGB', ...)
    
	return serve_pil_image(img)    
    


if __name__ == "__main__":
    app.run()
