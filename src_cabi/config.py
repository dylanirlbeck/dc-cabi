config = {
    ##############################
    # CaBi configuration         #
    ##############################

    # List of stations for which to render bike information
    'stations': [
        {
            # Florida Ave & R St NW
            'id': '0824960b-1f3f-11e7-bf6b-3863bb334450',
            'display_name': 'Florida'
        },

        {
            # North Capitol & R St NE
            'id': '2a76806e-32b4-4ec6-a851-f73ba7dafda1',
            'display_name': 'NorthCap'
        },

        {
            # 1st & Rhode Island Ave NW
            'id': '082515d4-1f3f-11e7-bf6b-3863bb334450',
            'display_name': '1st&Rhode'
        },

        {
            # Lincoln Rd & Seaton Pl NE/Harry Thomas Rec Center
            'id': '6d5ad96d-a704-4fa6-8b65-3ac643c5aa93',
            'display_name': 'Lincoln'
        }
    ],

    ###############################
    # Other values you probably
    # shouldn't touch
    ###############################

    # station_status information
    'cabi_api_url': 'https://gbfs.lyft.com/gbfs/2.3/dca-cabi/en/station_status.json',
}
