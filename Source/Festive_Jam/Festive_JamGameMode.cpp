// Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.

#include "Festive_JamGameMode.h"
#include "Festive_JamHUD.h"
#include "Festive_JamCharacter.h"
#include "UObject/ConstructorHelpers.h"

AFestive_JamGameMode::AFestive_JamGameMode()
	: Super()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnClassFinder(TEXT("/Game/FirstPersonCPP/Blueprints/FirstPersonCharacter"));
	DefaultPawnClass = PlayerPawnClassFinder.Class;

	// use our custom HUD class
	HUDClass = AFestive_JamHUD::StaticClass();
}
