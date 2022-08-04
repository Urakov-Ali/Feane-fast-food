console.log('ishlayabdi')

//we use js codes to take the id of the product
var updateBtns =document.getElementsByClassName('update-cart')

for(var i =0; i < updateBtns.lenght; i++){
	updateBtns[i].addEventListener('click',function(){
		var productId =this.dataset.product
		var action =this.dataset.action
		console.log('productId:', productId, "action:", action)

		console.log('User:', user)
		if(user == 'AnonymusUser'){
			console.log('Not logging in')
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action) {
	console.log('User is liggin')

	var url ='/update_item/'
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type':'application/json',
			'X-CSRF Token':csrftoken

		},
		body:JSON.stringify({'productId':productId, 'action':action})
	})
	.then((response) =>{
		return response.json()
	})
	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}